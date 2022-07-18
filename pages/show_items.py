from PRM_DATA import settings
from data.models import Item, Survey


def show_multi_line_free_text(item):
    return item

def show_survey():
    context = {}
    # Get all items
    items = Item.objects.all()
    context['items'] = items
    survey = Survey.objects.get(id=items[0].survey_id)
    context['survey'] = survey
    return context
