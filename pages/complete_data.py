from datetime import datetime

import cx_Oracle
import sqlite3
import time

from django.conf import settings
from django.utils.timezone import now
from tqdm import tqdm

QST = 'question.sqlite3'
# CRF = 'john_crf.sqlite3'

tables = [
    {
        "local_table": "respondent",
        "oracle_table": "prm_vw_respondent",
        "database": QST,
        "date_field": "mtdatum"
    },
    {
        "local_table": "spss_data",
        "oracle_table": "prm_vw_spss_data",
        "database": QST,
        "date_field": "mtdatum"
    }
]


def do_insert(sqlite_cur, table, cols_string, quest_string, ora_row):
    sql = f'''insert into {table} ({cols_string}) values ({quest_string})'''
    sqlite_cur.execute(sql, ora_row)


def get_latest_date(cur, date_field, table):
    sql = f'select max({date_field}) as max_date from {table}'
    for row in cur.execute(sql):
        max_date = row[0]
        # If date is string...
        if isinstance(max_date, str):
            max_date = datetime.strptime(max_date, '%Y-%m-%d %H:%M:%S')
        return max_date


def get_latest_date_local(cur, table):
    return get_latest_date(cur, table["date_field"], table["local_table"])


def get_latest_date_oracle(cur, table):
    return get_latest_date(cur, table["date_field"], table["oracle_table"])


# Append data from Oracle to local table
# Let op! In spss_data hebben records soms hetzelfde tijdstip
def fetch_and_append_data(table, ora_cur, sqlite_con, latest_date_local):
    start_time = time.time()

    # Get nr of Oracle records
    sql = f"select count(*) from {table['oracle_table']} where mtdatum > to_date('{latest_date_local}', 'YYYY-MM-DD HH24:MI:SS')"
    ora_cur.execute(sql)
    for row in ora_cur.execute(sql):
        n_recs = row[0]
        print(f'\n{table["oracle_table"]}: {n_recs} records')
        if n_recs == 0:
            return 'No records found!'

    # initialize bar
    bf = "{percentage:3.0f}%|{bar:80}| {n_fmt}/{total_fmt} {elapsed}"
    pbar = tqdm(total=n_recs, ncols=140, bar_format=bf)

    # Prepare columns string
    sqlite_cur = sqlite_con.cursor()
    sql = f'select * from {table["local_table"]}'
    sqlite_cur.execute(sql)

    cols = []
    for column in sqlite_cur.description:
        cols.append(column[0])
    cols_as_string = ','.join(cols).lower()

    # Prepare question string
    quest = '?,'
    quest_as_string = (quest * len(cols))[:-1]

    # Get data
    sql = f"select * from {table['oracle_table']} where mtdatum > to_date('{latest_date_local}', 'YYYY-MM-DD HH24:MI:SS')"
    ora_cur.execute(sql)

    # Process data => insert into local database
    for row in ora_cur.execute(sql):
        do_insert(sqlite_cur, table["local_table"], cols_as_string, quest_as_string,
                  row)
        pbar.update(1)
    sqlite_con.commit()
    pbar.close()
    elapsed_secs = time.time() - start_time
    return f'Fetched "{n_recs}" records in {elapsed_secs:.2f} seconds...'


# Complete the imported data only for respondents and spss_data
# Check last date
def complete_data():
    # Connect to Oracle: user, pwd, hostname/servicename
    user = settings.USER
    pw = settings.PW
    host = settings.HOST
    service_name = settings.SERVICE_NAME
    try:
        ora_con = cx_Oracle.connect(user, pw, f'{host}/{service_name}')
    except Exception as e:
        print(e)
        return
    ora_cur = ora_con.cursor()

    context = {}
    opmerkingen = []
    opmerkingen.append('Completing respondents and spss_data for all surveys...')

    for table in tables:
        sqlite_con = sqlite3.connect(table['database'])
        sqlite_cur = sqlite_con.cursor()
        latest_date_oracle = get_latest_date_oracle(ora_cur, table)
        latest_date_local = get_latest_date_local(sqlite_cur, table)
        # Do we need to fetch data and append?
        if latest_date_oracle > latest_date_local:
            opmerkingen.append(f'Fetching data for "{table["local_table"]}"...')
            opmerkingen.append(
                fetch_and_append_data(table, ora_cur, sqlite_con, latest_date_local))
        else:
            opmerkingen.append(f'No data to fetch for "{table["local_table"]}"...')
    context['opmerkingen'] = opmerkingen
    return context
