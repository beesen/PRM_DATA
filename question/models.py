from django.db import models

# Create your models here.
class Respondent(models.Model):
    # id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    lijst_id = models.IntegerField(db_column='LIJST_ID', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    naam = models.TextField(db_column='NAAM', blank=True, null=True)  # Field name made lowercase.
    anr = models.TextField(db_column='ANR', blank=True, null=True)  # Field name made lowercase.
    mtdatum = models.TextField(db_column='MTDATUM', blank=True, null=True)  # Field name made lowercase.
    mtanr = models.IntegerField(db_column='MTANR', blank=True, null=True)  # Field name made lowercase.
    uitnoddatum = models.TextField(db_column='UITNODDATUM', blank=True, null=True)  # Field name made lowercase.
    einddatum = models.TextField(db_column='EINDDATUM', blank=True, null=True)  # Field name made lowercase.
    begindatum = models.TextField(db_column='BEGINDATUM', blank=True, null=True)  # Field name made lowercase.
    volgnr = models.IntegerField(db_column='VOLGNR', blank=True, null=True)  # Field name made lowercase.
    zoveelstekeer = models.IntegerField(db_column='ZOVEELSTEKEER', blank=True, null=True)  # Field name made lowercase.
    extra = models.TextField(db_column='EXTRA', blank=True, null=True)  # Field name made lowercase.
    kenmerk = models.TextField(db_column='KENMERK', blank=True, null=True)  # Field name made lowercase.
    taal_id = models.IntegerField(db_column='TAAL_ID', blank=True, null=True)  # Field name made lowercase.
    reminderdatum = models.TextField(db_column='REMINDERDATUM', blank=True, null=True)  # Field name made lowercase.
    batchuitnod1 = models.TextField(db_column='BATCHUITNOD1', blank=True, null=True)  # Field name made lowercase.
    batchuitnod2 = models.TextField(db_column='BATCHUITNOD2', blank=True, null=True)  # Field name made lowercase.
    npm_respondent_id = models.FloatField(db_column='NPM_RESPONDENT_ID', blank=True, null=True)  # Field name made lowercase.
    fillin_role = models.IntegerField(db_column='FILLIN_ROLE', blank=True, null=True)  # Field name made lowercase.
    seq_nr = models.IntegerField(db_column='SEQ_NR', blank=True, null=True)  # Field name made lowercase.
    conv_dt = models.TextField(db_column='CONV_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESPONDENT'


class Soort(models.Model):
    # id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    naam = models.TextField(db_column='NAAM', blank=True, null=True)  # Field name made lowercase.
    oms = models.TextField(db_column='OMS', blank=True, null=True)  # Field name made lowercase.
    mtdatum = models.TextField(db_column='MTDATUM', blank=True, null=True)  # Field name made lowercase.
    mtanr = models.IntegerField(db_column='MTANR', blank=True, null=True)  # Field name made lowercase.
    img = models.TextField(db_column='IMG', blank=True, null=True)  # Field name made lowercase.
    help_id = models.IntegerField(db_column='HELP_ID', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
    single_answer = models.TextField(db_column='SINGLE_ANSWER', blank=True, null=True)  # Field name made lowercase.
    spss_format = models.TextField(db_column='SPSS_FORMAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOORT'


class SpssData(models.Model):
    lijst_id = models.IntegerField(db_column='LIJST_ID', blank=True, null=True)  # Field name made lowercase.
    respondent_id = models.IntegerField(db_column='RESPONDENT_ID', blank=True, null=True)  # Field name made lowercase.
    volgnr = models.IntegerField(db_column='VOLGNR', blank=True, null=True)  # Field name made lowercase.
    antwoord = models.TextField(db_column='ANTWOORD', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    zoveelstekeer = models.IntegerField(db_column='ZOVEELSTEKEER', blank=True, null=True)  # Field name made lowercase.
    soort_id = models.IntegerField(db_column='SOORT_ID', blank=True, null=True)  # Field name made lowercase.
    altern = models.TextField(db_column='ALTERN', blank=True, null=True)  # Field name made lowercase.
    spss_variabele = models.TextField(db_column='SPSS_VARIABELE', blank=True, null=True)  # Field name made lowercase.
    spss_missing_value = models.TextField(db_column='SPSS_MISSING_VALUE', blank=True, null=True)  # Field name made lowercase.
    spss_label = models.TextField(db_column='SPSS_LABEL', blank=True, null=True)  # Field name made lowercase.
    spss_data_type = models.TextField(db_column='SPSS_DATA_TYPE', blank=True, null=True)  # Field name made lowercase.
    spss_value_labels = models.TextField(db_column='SPSS_VALUE_LABELS', blank=True, null=True)  # Field name made lowercase.
    mtdatum = models.TextField(db_column='MTDATUM', blank=True, null=True)  # Field name made lowercase.
    subvolgnr = models.IntegerField(db_column='SUBVOLGNR', blank=True, null=True)  # Field name made lowercase.
    conv_dt = models.TextField(db_column='CONV_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SPSS_DATA'


class Vraag(models.Model):
    lijst_id = models.IntegerField(db_column='LIJST_ID', blank=True, null=True)  # Field name made lowercase.
    volgnr = models.IntegerField(db_column='VOLGNR', blank=True, null=True)  # Field name made lowercase.
    soort_id = models.IntegerField(db_column='SOORT_ID', blank=True, null=True)  # Field name made lowercase.
    tekst = models.TextField(db_column='TEKST', blank=True, null=True)  # Field name made lowercase.
    altern = models.TextField(db_column='ALTERN', blank=True, null=True)  # Field name made lowercase.
    vervolg = models.TextField(db_column='VERVOLG', blank=True, null=True)  # Field name made lowercase.
    min = models.IntegerField(db_column='MIN', blank=True, null=True)  # Field name made lowercase.
    max = models.IntegerField(db_column='MAX', blank=True, null=True)  # Field name made lowercase.
    mtdatum = models.TextField(db_column='MTDATUM', blank=True, null=True)  # Field name made lowercase.
    mtanr = models.IntegerField(db_column='MTANR', blank=True, null=True)  # Field name made lowercase.
    spss_variabele = models.TextField(db_column='SPSS_VARIABELE', blank=True, null=True)  # Field name made lowercase.
    spss_missing_value = models.TextField(db_column='SPSS_MISSING_VALUE', blank=True, null=True)  # Field name made lowercase.
    score = models.TextField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    categorie = models.TextField(db_column='CATEGORIE', blank=True, null=True)  # Field name made lowercase.
    spss_label = models.TextField(db_column='SPSS_LABEL', blank=True, null=True)  # Field name made lowercase.
    header = models.TextField(db_column='HEADER', blank=True, null=True)  # Field name made lowercase.
    footer = models.TextField(db_column='FOOTER', blank=True, null=True)  # Field name made lowercase.
    tekst_uitgebreid = models.TextField(db_column='TEKST_UITGEBREID', blank=True, null=True)  # Field name made lowercase.
    afbreekwaarde = models.TextField(db_column='AFBREEKWAARDE', blank=True, null=True)  # Field name made lowercase.
    altern_uk = models.TextField(db_column='ALTERN_UK', blank=True, null=True)  # Field name made lowercase.
    header_uk = models.TextField(db_column='HEADER_UK', blank=True, null=True)  # Field name made lowercase.
    footer_uk = models.TextField(db_column='FOOTER_UK', blank=True, null=True)  # Field name made lowercase.
    tekst_uk = models.TextField(db_column='TEKST_UK', blank=True, null=True)  # Field name made lowercase.
    tekst_uitgebr_uk = models.TextField(db_column='TEKST_UITGEBR_UK', blank=True, null=True)  # Field name made lowercase.
    warehouse = models.TextField(db_column='WAREHOUSE', blank=True, null=True)  # Field name made lowercase.
    header_papier = models.TextField(db_column='HEADER_PAPIER', blank=True, null=True)  # Field name made lowercase.
    header_papier_uk = models.TextField(db_column='HEADER_PAPIER_UK', blank=True, null=True)  # Field name made lowercase.
    checkquestion = models.TextField(db_column='CHECKQUESTION', blank=True, null=True)  # Field name made lowercase.
    from_list = models.IntegerField(db_column='FROM_LIST', blank=True, null=True)  # Field name made lowercase.
    q_comment = models.TextField(db_column='Q_COMMENT', blank=True, null=True)  # Field name made lowercase.
    spss_missing_2 = models.TextField(db_column='SPSS_MISSING_2', blank=True, null=True)  # Field name made lowercase.
    n_subquest = models.IntegerField(db_column='N_SUBQUEST', blank=True, null=True)  # Field name made lowercase.
    spss_format = models.TextField(db_column='SPSS_FORMAT', blank=True, null=True)  # Field name made lowercase.
    opmerking = models.TextField(db_column='OPMERKING', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VRAAG'


class Vragenlijst(models.Model):
    # id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    beheerder_id = models.IntegerField(db_column='BEHEERDER_ID', blank=True, null=True)  # Field name made lowercase.
    naam = models.TextField(db_column='NAAM', blank=True, null=True)  # Field name made lowercase.
    begin_datum = models.TextField(db_column='BEGIN_DATUM', blank=True, null=True)  # Field name made lowercase.
    eind_datum = models.TextField(db_column='EIND_DATUM', blank=True, null=True)  # Field name made lowercase.
    proloog = models.TextField(db_column='PROLOOG', blank=True, null=True)  # Field name made lowercase.
    epiloog = models.TextField(db_column='EPILOOG', blank=True, null=True)  # Field name made lowercase.
    terug_mag = models.TextField(db_column='TERUG_MAG', blank=True, null=True)  # Field name made lowercase.
    lastdate = models.TextField(db_column='LASTDATE', blank=True, null=True)  # Field name made lowercase.
    lastuser = models.TextField(db_column='LASTUSER', blank=True, null=True)  # Field name made lowercase.
    mtdatum = models.TextField(db_column='MTDATUM', blank=True, null=True)  # Field name made lowercase.
    mtanr = models.IntegerField(db_column='MTANR', blank=True, null=True)  # Field name made lowercase.
    uitnoddatum = models.TextField(db_column='UITNODDATUM', blank=True, null=True)  # Field name made lowercase.
    uitnodtekst = models.TextField(db_column='UITNODTEKST', blank=True, null=True)  # Field name made lowercase.
    taal_id = models.IntegerField(db_column='TAAL_ID', blank=True, null=True)  # Field name made lowercase.
    aantalkeer = models.IntegerField(db_column='AANTALKEER', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    random_id = models.IntegerField(db_column='RANDOM_ID', blank=True, null=True)  # Field name made lowercase.
    buttons_left = models.TextField(db_column='BUTTONS_LEFT', blank=True, null=True)  # Field name made lowercase.
    epiloog_uk = models.TextField(db_column='EPILOOG_UK', blank=True, null=True)  # Field name made lowercase.
    nl_versie = models.TextField(db_column='NL_VERSIE', blank=True, null=True)  # Field name made lowercase.
    uk_versie = models.TextField(db_column='UK_VERSIE', blank=True, null=True)  # Field name made lowercase.
    invite_mode = models.IntegerField(db_column='INVITE_MODE', blank=True, null=True)  # Field name made lowercase.
    uitnodlogin = models.TextField(db_column='UITNODLOGIN', blank=True, null=True)  # Field name made lowercase.
    uitnodletter = models.TextField(db_column='UITNODLETTER', blank=True, null=True)  # Field name made lowercase.
    afzender = models.TextField(db_column='AFZENDER', blank=True, null=True)  # Field name made lowercase.
    maxmail = models.IntegerField(db_column='MAXMAIL', blank=True, null=True)  # Field name made lowercase.
    semester = models.TextField(db_column='SEMESTER', blank=True, null=True)  # Field name made lowercase.
    cursusjaar = models.TextField(db_column='CURSUSJAAR', blank=True, null=True)  # Field name made lowercase.
    remindertekst = models.TextField(db_column='REMINDERTEKST', blank=True, null=True)  # Field name made lowercase.
    reminderlogin = models.TextField(db_column='REMINDERLOGIN', blank=True, null=True)  # Field name made lowercase.
    reminderletter = models.TextField(db_column='REMINDERLETTER', blank=True, null=True)  # Field name made lowercase.
    autoreminder = models.TextField(db_column='AUTOREMINDER', blank=True, null=True)  # Field name made lowercase.
    reminderdate = models.TextField(db_column='REMINDERDATE', blank=True, null=True)  # Field name made lowercase.
    rnd_select = models.TextField(db_column='RND_SELECT', blank=True, null=True)  # Field name made lowercase.
    medpsy_set = models.TextField(db_column='MEDPSY_SET', blank=True, null=True)  # Field name made lowercase.
    printlogo = models.TextField(db_column='PRINTLOGO', blank=True, null=True)  # Field name made lowercase.
    invite_rem_mode = models.IntegerField(db_column='INVITE_REM_MODE', blank=True, null=True)  # Field name made lowercase.
    answer_check = models.TextField(db_column='ANSWER_CHECK', blank=True, null=True)  # Field name made lowercase.
    userlink = models.TextField(db_column='USERLINK', blank=True, null=True)  # Field name made lowercase.
    progress_on = models.TextField(db_column='PROGRESS_ON', blank=True, null=True)  # Field name made lowercase.
    music_file = models.TextField(db_column='MUSIC_FILE', blank=True, null=True)  # Field name made lowercase.
    do_music = models.TextField(db_column='DO_MUSIC', blank=True, null=True)  # Field name made lowercase.
    bar_on = models.TextField(db_column='BAR_ON', blank=True, null=True)  # Field name made lowercase.
    tx = models.TextField(db_column='TX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VRAGENLIJST'
