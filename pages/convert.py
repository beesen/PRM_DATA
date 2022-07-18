# Create your views here.
from django.conf import settings

from data.models import Item, Survey
from pages.utils import to_multi_line_free_text, to_multiple_choice_single_answer, \
    to_single_line_free_text, to_notes, count_statements, to_scale_rank, get_survey_id, \
    to_multiple_choice_multiple_answer
from question.models import Soort, Vraag

# Check scores for soort_id=15
def check_scores(vragen):
    vragenx = vragen.filter(soort_id=15)
    for vraagx in vragenx:
        if vraagx.score:
            scores = vraagx.score.split('#')
            score0 = scores[0]
            for s in range(2, len(scores)):
                if scores[s] != score0:
                    return False, f"{vraagx.lijst_id}, {vraagx.volgnr}"
        else:
            return False, f"{vraagx.lijst_id}, {vraagx.volgnr}"
    return True, ''

def convert():
    if settings.DO_NOT_IMPORT:
        return
    # Clean items
    Item.objects.all().delete()

    context = {}
    lijst_id = settings.SURVEY_ID
    id = get_survey_id(lijst_id=lijst_id)
    context['lijst'] = Survey.objects.get(id=id).name
    vragen = Vraag.objects.using('npm').order_by('lijst_id', 'volgnr')
    vragen = vragen.filter(lijst_id=lijst_id).order_by('volgnr')
    ok, msg = check_scores(vragen)
    if not ok:
        context['opmerkingen'] = [f'<span style="color:red; font-weight:bold">Controleer de scores van soort_id 15 {msg}...</span>']
        return context

    # vragen = vragen.filter(volgnr=2)
    # Let op: "vragen" NIET gebruiken, vanwege de order by!
    soorten = Vraag.objects.using('npm').all().values_list('soort_id',
                                                           flat=True).distinct()
    context['soorten'] = Soort.objects.using('npm').filter(id__in=soorten)
    # context['vragen'] = vragen
    opmerkingen = []
    # Loop over alle soorten
    for vraag in vragen:
        opmerking = f'Vraag {vraag.lijst_id} - {vraag.volgnr} / {vragen.count()} / {vraag.soort_id} - '
        try:
            if vraag.soort_id == 1:  # OPEN ANSWER (MORE LINES, HORIZONTAL)
                extra = to_multi_line_free_text(vraag)
            elif vraag.soort_id == 2:  # MULTIPLE CHOICE, RADIO BUTTONS (VERTICAL)
                extra = to_multiple_choice_single_answer(vraag, 'vertical', False)
            elif vraag.soort_id == 3:  # MULTIPLE CHOICE, RADIO BUTTONS (HORIZONTAL)
                if False and vraag.lijst_id == 2240 and vraag.volgnr == 3:
                    extra = to_multiple_choice_single_answer(vraag, 'horizontal', True)
                else:
                    extra = to_multiple_choice_single_answer(vraag, 'horizontal', False)
            elif vraag.soort_id == 5:  # MULTIPLE CHOICE, CHECK BOXES (VERTICAL)
                extra = to_multiple_choice_multiple_answer(vraag, 'vertical', False)
            elif vraag.soort_id == 6:  # OPEN ANSWER (MEER REGELS, VERTICAL)
                extra = to_multi_line_free_text(vraag)
            elif vraag.soort_id == 7:  # OPEN ANSWER (1 LINE, HORIZONTAL)
                extra = to_single_line_free_text(vraag, 1)
            elif vraag.soort_id == 8:  # MEDEDELING ( < 4000)
                extra = to_notes(vraag)
            elif vraag.soort_id == 9:  # NUMERICAL (1 LINE, HORIZONTAL)
                extra = to_single_line_free_text(vraag, 2)
            elif vraag.soort_id == 15:  # MATRIX RADIO INPUT
                nr_of_statements = count_statements(vraag)
                if nr_of_statements == 1:
                    extra = to_multiple_choice_single_answer(vraag, 'horizontal', False)
                    extra = extra + ' vraagtype gewijzigd naar "Multiple choice single answer"'
                else:
                    extra = to_scale_rank(vraag)
            elif vraag.soort_id == 21:  # MULTIPLE QUESTION (VERTICAL)
                nr_of_statements = count_statements(vraag)
                if nr_of_statements == 1:
                    extra = to_multiple_choice_single_answer(vraag, 'vertical', False)
                    extra = extra + ' vraagtype gewijzigd naar "Multiple choice single answer"'
                else:
                    extra = f' Soort {vraag.soort_id} nog niet behandeld...'
            elif vraag.soort_id == 36:  # MULTI OPEN ANSWER (1 LINE, HORIZONTAL)
                extra = to_single_line_free_text(vraag, 2)
            elif vraag.soort_id == 37:  # DATE INPUT (NO POPUP)
                extra = to_single_line_free_text(vraag, 3)
            else:
                extra = f' Soort {vraag.soort_id} nog niet behandeld...'
        except Exception as e:
            extra = f' "{e}" ...'
        if extra[0:2] == 'Ok':
            opmerking = opmerking + extra
        else:
            opmerking = opmerking + '<span style="color:red; font-weight:bold">' + extra + '</span>'
        opmerkingen.append(opmerking)
    context['opmerkingen'] = opmerkingen
    return context
