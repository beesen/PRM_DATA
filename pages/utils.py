import re
from data.models import Item, Survey, ItemOption, ItemStatement


def get_survey_id(lijst_id):
    survey = Survey.objects.filter(name__contains=lijst_id)
    return survey[0].id


# Return nr of statements found
def count_statements(vraag):
    return vraag.tekst.count('|') + 1


# Return nr of options found
def count_options(vraag):
    return vraag.altern.count('|') + 1


# returns a new string after removing
# HTML tags
# leading, trailing whitespaces,
# new lines (\n) and tabs (\t)
# and series of characters at beginning of string (12a.)
def clean_str(str):
    if '<' in str:
        # Remove HTML tags <>
        pattern = r'<.*?>'
        flags = re.DOTALL + re.MULTILINE
        clean = re.compile(pattern, flags)
        help = re.sub(clean, '', str)
    else:
        help = str
    help = help.strip()
    # Remove LF
    help = help.replace('\n', '')
    # Remove TAB
    help = help.replace('\t', '')
    if help[0].isdigit():
        # Remove digit(s) and dot at beginning
        pattern = r'^\d+[a-zA-Z]*\.?'
        clean_str = re.compile(pattern)
        help = re.sub(clean_str, '', help)
        help = help.strip()
    return help


def to_multi_line_free_text(vraag):
    answer_type_id = 1
    item_type_id = 1
    survey_id = get_survey_id(vraag.lijst_id)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=vraag.tekst,
                               page_nr=vraag.volgnr, next_page=vraag.vervolg)
    return 'Ok'


def to_single_line_free_text(vraag, answer_type_id):
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
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               page_nr=vraag.volgnr, next_page=vraag.vervolg)
    return msg


def to_notes(vraag):
    answer_type_id = 1
    item_type_id = 5
    survey_id = get_survey_id(vraag.lijst_id)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=vraag.tekst,
                               page_nr=vraag.volgnr, next_page=vraag.vervolg)
    return 'Ok'


def to_multiple_choice_single_answer(vraag, display_direction, add_text_box_other):
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
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               page_nr=vraag.volgnr, next_page=-1)
    save_options(vraag, item)
    return msg


# Save options for this item
def save_options(vraag, item):
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
        item_option = ItemOption.objects.create(
            seq_nr=n + 1, option_text=clean_str(option_text[n]), item_id=item.id,
            next_page=next_page)


# Save statements for this item
def save_statements(vraag, item):
    nr_of_statements = count_statements(vraag)
    statement_texts = vraag.tekst.split('|')
    for n in range(nr_of_statements):
        text = clean_str(statement_texts[n])
        item_statement = ItemStatement.objects.create(
            seq_nr=n + 1, statement_text=text, item_id=item.id)


def to_scale_rank(vraag):
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
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text,
                               page_nr=vraag.volgnr, next_page=-1)
    save_options(vraag, item)
    save_statements(vraag, item)
    return msg
