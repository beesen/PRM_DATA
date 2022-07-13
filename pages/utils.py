import re
from data.models import Item, Survey, ItemOption, ItemStatement
from question.models import Vraag


def get_survey_id(lijst_id: int):
    survey = Survey.objects.filter(name__contains=lijst_id)
    return survey[0].id


# Return nr of statements found
def count_statements(vraag: Vraag):
    return vraag.tekst.count('|') + 1


# Return nr of options found
def count_options(vraag: Vraag):
    return vraag.altern.count('|') + 1


# returns a new string after removing
# leading, trailing whitespaces,
# new lines (\n) and tabs (\t)
# and series of characters at beginning of string (12a.)
def clean_number(str: str):
    help = str.strip()
    # Remove LF
    help = help.replace('\n', '')
    # Remove TAB
    help = help.replace('\t', '')
    # Remove blank
    help = help.replace('&nbsp;', '')
    if help[0].isdigit() and not help.isnumeric():
        # Als er een punt zit aan begin van de string
        # TODO: verfijnen?
        if '.' in help[0:4]:
            # Remove digit(s) and dot at beginning
            pattern = r'^\d+[a-zA-Z]*\.{1}'
        else:
            # Remove digit(s) at beginning
            pattern = r'^\d+'
        clean_str = re.compile(pattern)
        help = re.sub(clean_str, '', help)
        help = help.strip()
    return help


# returns a new string after removing
# HTML tags
# leading, trailing whitespaces,
# new lines (\n) and tabs (\t)
# and series of characters at beginning of string (12a.)
def clean_str(str: str):
    if '<' in str:
        # Remove HTML tags <>
        pattern = r'<.*?>'
        flags = re.DOTALL + re.MULTILINE
        clean = re.compile(pattern, flags)
        help = re.sub(clean, '', str)
    else:
        help = str
    help = clean_number(help)
    return help


def to_multi_line_free_text(vraag: Vraag):
    answer_type_id = 1
    item_type_id = 1
    survey_id = get_survey_id(vraag.lijst_id)
    if vraag.tekst:
        item_text = vraag.tekst
        msg = 'Ok'
    else:
        item_text = ''
        msg = 'Ok - geen tekst'
    if vraag.header:
        item_text = item_text + vraag.header
        msg = 'Ok - header aanwezig'
    item_text = clean_number(item_text)
    spss_variable = vraag.spss_variabele
    spss_variable_label = vraag.spss_label
    spss_missing_value = vraag.spss_missing_value
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               page_nr=vraag.volgnr, next_page=vraag.vervolg,
                               spss_variable=spss_variable,
                               spss_variable_label=spss_variable_label,
                               spss_missing_value=spss_missing_value)
    return 'Ok'


def to_single_line_free_text(vraag: Vraag, answer_type_id: int):
    item_type_id = 4
    survey_id = get_survey_id(vraag.lijst_id)
    if vraag.tekst:
        item_text = vraag.tekst
        msg = 'Ok'
    else:
        item_text = ''
        msg = 'Ok - geen tekst'
    if vraag.header:
        item_text = item_text + vraag.header
        msg = 'Ok - header aanwezig'
    item_text = clean_number(item_text)
    spss_variable = vraag.spss_variabele
    spss_variable_label = vraag.spss_label
    spss_missing_value = vraag.spss_missing_value
    if answer_type_id == 2:
        spss_format = 'N4'
    elif answer_type_id == 3:
        spss_format = 'DATE10'
    else:
        spss_format = 'A100'
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               page_nr=vraag.volgnr, next_page=vraag.vervolg,
                               spss_variable=spss_variable,
                               spss_variable_label=spss_variable_label,
                               spss_missing_value=spss_missing_value,
                               spss_format=spss_format)
    return msg


def to_notes(vraag: Vraag):
    answer_type_id = 1
    item_type_id = 5
    survey_id = get_survey_id(vraag.lijst_id)
    item_text = clean_number(vraag.tekst)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               page_nr=vraag.volgnr, next_page=vraag.vervolg)
    return 'Ok'


def to_multiple_choice_single_answer(vraag: Vraag, display_direction: str,
                                     add_text_box_other: bool):
    answer_type_id = 2
    item_type_id = 2
    survey_id = get_survey_id(vraag.lijst_id)
    if vraag.tekst:
        item_text = vraag.tekst
        msg = 'Ok'
    else:
        item_text = ''
        msg = 'Ok - geen tekst'
    if vraag.header:
        item_text = item_text + vraag.header
        msg = 'Ok - header aanwezig'
    item_text = clean_number(item_text)
    spss_variable = vraag.spss_variabele
    spss_variable_label = vraag.spss_label
    spss_missing_value = vraag.spss_missing_value
    spss_format = 'N4'
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               display_direction=display_direction,
                               add_text_box_other=add_text_box_other,
                               page_nr=vraag.volgnr, next_page=-1,
                               spss_variable=spss_variable,
                               spss_variable_label=spss_variable_label,
                               spss_missing_value=spss_missing_value,
                               spss_format=spss_format)
    save_options(vraag, item)
    return msg


# Save options for this item
def save_options(vraag: Vraag, item):
    nr_of_options = count_options(vraag)
    option_text = vraag.altern.split('|')
    if len(option_text) != nr_of_options:
        raise Exception('Error in field "altern"')
    next_pages = vraag.vervolg.split('|')
    if len(next_pages) == 1:
        # Herhaal x keer
        for n in range(nr_of_options - 1):
            next_pages.append(next_pages[0])
    else:
        if len(next_pages) != nr_of_options:
            raise Exception('Error in field "vervolg"')
    for n in range(nr_of_options):
        next_page = next_pages[n].strip()
        text = clean_str(option_text[n])
        item_option = ItemOption.objects.create(
            seq_nr=n + 1, option_text=text, item_id=item.id,
            next_page=next_page,
            spss_value_label=text)


# Save statements for this item
def save_statements(vraag: Vraag, item):
    nr_of_statements = count_statements(vraag)
    statement_texts = vraag.tekst.split('|')
    spss_variables = vraag.spss_variabele.split('#')
    spss_variable_labels = vraag.spss_label.split('#')
    for n in range(nr_of_statements):
        text = clean_str(statement_texts[n])
        spss_variable = clean_str(spss_variables[n])
        spss_variable_label = clean_str(spss_variable_labels[n])
        spss_missing_value = '9999'
        spss_format = 'N4'
        item_statement = ItemStatement.objects.create(
            seq_nr=n + 1, statement_text=text, item_id=item.id,
            spss_variable=spss_variable,
            spss_variable_label=spss_variable_label,
            spss_missing_value=spss_missing_value,
            spss_format=spss_format
        )


def to_multiple_choice_multiple_answer(vraag: Vraag, display_direction: str,
                                       add_text_box_other: bool):
    answer_type_id = 2
    item_type_id = 3
    survey_id = get_survey_id(vraag.lijst_id)
    if vraag.tekst:
        item_text = vraag.tekst
        msg = 'Ok'
    else:
        item_text = ''
        msg = 'Ok - geen tekst'
    if vraag.header:
        item_text = item_text + vraag.header
        msg = 'Ok - header aanwezig'
    item_text = clean_number(item_text)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               display_direction=display_direction,
                               add_text_box_other=add_text_box_other,
                               page_nr=vraag.volgnr, next_page=-1)
    save_options(vraag, item)
    return msg


def to_scale_rank(vraag: Vraag):
    answer_type_id = 2
    item_type_id = 6
    survey_id = get_survey_id(vraag.lijst_id)
    if vraag.header:
        item_text = vraag.header
    else:
        msg = 'Ok - geen header aanwezig'
        item_text = ' '
    if vraag.footer:
        msg = 'Ok - footer aanwezig'
    else:
        msg = 'Ok'
    item_text = clean_number(item_text)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               page_nr=vraag.volgnr, next_page=-1)
    save_options(vraag, item)
    save_statements(vraag, item)
    return msg
