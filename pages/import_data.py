import cx_Oracle
import sqlite3
import time

from django.conf import settings
from tqdm import tqdm

QST = 'question.sqlite3'
# CRF = 'john_crf.sqlite3'

pairs = [
    # Eerst locale tabellen, daarna views van Oracle!
    # Voor CRF geldt: kijk in avw_crf_spss_data
    # ('crf_pages', 'avw_crf_pages', CRF),
    # ('crf_respondents', 'avw_crf_respondents', CRF),
    # ('crf_spss_data', 'avw_crf_spss_data', CRF),
    # ('crf_vraag', 'avw_crf_vraag', CRF),
     ('vragenlijst', 'prm_vw_vragenlijst', QST),
     ('vraag', 'prm_vw_vraag', QST),
     ('soort', 'prm_vw_soort', QST),
     ('respondent', 'prm_vw_respondent', QST),
     # ('spss_data', 'prm_vw_spss_data', QST)
]
def do_insert(sqlite_cur, table, cols_string, quest_string, ora_row):
    sql = f'''insert into {table} ({cols_string}) values ({quest_string})'''
    sqlite_cur.execute(sql, ora_row)


def show_aggr(sqlite_cur):
    sql = 'select "T"||cast (meetmoment-1 as text) as T, page, count(*) from crf_spss_data sd, CRF_PAGES_TABLE p where sd.EXTERNAL_ID = p.EXTERNAL_ID group by meetmoment, sd.external_id order by meetmoment, sd.external_id;'
    sqlite_cur.execute(sql)
    print('T0', 'Page', 'Nr recs')
    for row in sqlite_cur.execute(sql):
        print(row)


def import_data():
    if settings.DO_NOT_BURN:
        return
    # Connect to Oracle: user, pwd, hostname/servicename
    user = settings.USER
    pw = settings.PW
    host = settings.HOST
    service_name = settings.SERVICE_NAME
    ora_con = cx_Oracle.connect(user, pw, f'{host}/{service_name}')
    ora_cur = ora_con.cursor()

    for pair in pairs:
        start_time = time.time()
        sqlite_con = sqlite3.connect(pair[2])
        sqlite_cur = sqlite_con.cursor()

        # Get nr of records
        sql = f'select count(*) from {pair[1]}'
        ora_cur.execute(sql)
        for row in ora_cur.execute(sql):
            n_recs = row[0]
            print(f'\n{pair[1]}: {n_recs} records')

        # initialize bar
        bf = "{percentage:3.0f}%|{bar:80}| {n_fmt}/{total_fmt} {elapsed}"
        pbar = tqdm(total=n_recs, ncols=140, bar_format=bf)

        if 1 == 1:
            # Empty table
            sql = f'delete from {pair[0]}'
            sqlite_cur.execute(sql)
            sqlite_con.commit()

            # Prepare columns string
            sql = f'select * from {pair[0]}'
            sqlite_cur.execute(sql)

            cols = []
            for column in sqlite_cur.description:
                cols.append(column[0])
            cols_as_string = ','.join(cols).lower()

            # Prepare question string
            quest = '?,'
            quest_as_string = (quest * len(cols))[:-1]

            # Get data
            sql = f'select * from {pair[1]}'
            ora_cur.execute(sql)

            # Process data => insert into local database
            for row in ora_cur.execute(sql):
                do_insert(sqlite_con, pair[0], cols_as_string, quest_as_string, row)
                pbar.update(1)
            sqlite_con.commit()
            pbar.close()

            # if pair[0]=='crf_spss_data':
            #     show_aggr(sqlite_cur)

            elapsed_secs = time.time() - start_time
            print(f' Elapsed time {elapsed_secs:.2f} seconds')
