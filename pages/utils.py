from data.models import Item, Survey, ItemOption


def get_survey_id(lijst_id):
    survey = Survey.objects.filter(name__contains=lijst_id)
    return survey[0].id


# Return nr of statements found
def count_statements(vraag):
    return vraag.tekst.count('|') + 1


# Return nr of options found
def count_options(vraag):
    return vraag.altern.count('|') + 1


def to_multi_line_free_text(vraag):
    answer_type_id = 1
    item_type_id = 1
    survey_id = get_survey_id(vraag.lijst_id)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=vraag.tekst)
    return 'Ok'


def to_single_line_free_text(vraag, answer_type_id):
    item_type_id = 4
    survey_id = get_survey_id(vraag.lijst_id)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=vraag.tekst)
    return 'Ok'


def to_notes(vraag):
    answer_type_id = 1
    item_type_id = 5
    survey_id = get_survey_id(vraag.lijst_id)
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=vraag.tekst)
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
                               survey_id=survey_id, item_text=item_text)
    return msg


# Save options for this item
def save_options(vraag, item):
    nr_of_options = count_options(vraag)
    for n in range(nr_of_options):
        option_text = vraag.altern.split('|')
        item_option = ItemOption.objects.create(
            seq_nr=n, option_text=option_text, item_id=item.id)


# Save statements for this item
def save_statements(vraag, item):
    None


def to_scale_rank(vraag):
    answer_type_id = 2
    item_type_id = 6
    survey_id = get_survey_id(vraag.lijst_id)
    item_text = vraag.header
    if vraag.footer:
        msg = 'Ok - footer aanwezig'
    item = Item.objects.create(seq_nr=vraag.volgnr, answer_type_id=answer_type_id,
                               item_type_id=item_type_id,
                               survey_id=survey_id, item_text=item_text)
    save_options(vraag, item)
    save_statements(vraag, item)
