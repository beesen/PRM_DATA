from PRM_DATA import settings
from data.models import Item, Survey


def show_multi_line_free_text(item):
    return item

def show_items():
    context = {}
    survey = Survey.objects.get(name__contains=settings.SURVEY_ID)
    context['survey'] = survey
    # Get items of this survey
    items = Item.objects.filter(survey_id=survey.id)
    context['items'] = items
    return context
