from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
from data.models import Item
from pages.utils import to_multi_line_free_text, to_multiple_choice_single_answer, \
    to_single_line_free_text, to_notes, count_statements, to_scale_rank
from question.models import Soort, Vraag


def home_view(request: WSGIRequest):
    return render(request, template_name='pages/home.html', context={})


def fill_view(request: WSGIRequest):
    # Clean items
    Item.objects.all().delete()

    context = {}
    vragen = Vraag.objects.using('npm').all().order_by('volgnr')
    # Let op: "vragen" NIET gebruiken, vanwege de order by!
    soorten = Vraag.objects.using('npm').all().values_list('soort_id',
                                                           flat=True).distinct()
    context['soorten'] = Soort.objects.using('npm').filter(id__in=soorten)
    # context['vragen'] = vragen
    opmerkingen = []
    # Loop over alle soorten
    j = 1
    for vraag in vragen:
        opmerking = f'Vraag {j}/{vragen.count()} - '

        if vraag.soort_id == 1:  # OPEN ANSWER (MORE LINES, HORIZONTAL)
            extra = to_multi_line_free_text(vraag)
        elif vraag.soort_id == 2:  # MULTIPLE CHOICE, RADIO BUTTONS (VERTICAL)
            extra = to_multiple_choice_single_answer(vraag, 'vertical', False)
        elif vraag.soort_id == 3:  # MULTIPLE CHOICE, RADIO BUTTONS (HORIZONTAL)
            extra = to_multiple_choice_single_answer(vraag, 'horizontal', False)
        elif vraag.soort_id == 5:  # MULTIPLE CHOICE, CHECK BOXES (VERTICAL)
            None
        elif vraag.soort_id == 6:  # OPEN ANSWER (MEER REGELS, VERTICAL)
            extra = to_multi_line_free_text(vraag)
        elif vraag.soort_id == 7:  # OPEN ANSWER (1 LINE, HORIZONTAL)
            extra = to_single_line_free_text(vraag, 1)
        elif vraag.soort_id == 8:  # MEDEDELING ( < 4000)
            extra = to_notes(vraag)
        elif vraag.soort_id == 9:  # OPEN ANSWER (1 LINE, HORIZONTAL)
            extra = to_single_line_free_text(vraag, 2)
        elif vraag.soort_id == 15:  # MATRIX RADIO INPUT
            nr_of_statements = count_statements(vraag)
            if nr_of_statements == 1:
                extra = to_multiple_choice_single_answer(vraag, 'horizontal', False)
                extra = extra + ' vraagtype gewijzigd naar "Multiple choice single answer"'
            else:
                extra = to_scale_rank(vraag)


        else:
            extra = f' Soort {vraag.soort_id} nog niet behandeld...'
        try:
            opmerkingen.append(opmerking + extra)
        except:
            print('Foutje bij vraag.volgnr...')
        j += 1
    context['opmerkingen'] = opmerkingen
    return render(request, template_name='pages/fill.html', context=context)
