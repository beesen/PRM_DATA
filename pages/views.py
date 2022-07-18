from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from pages.incremental_import import incremental_import
from pages.convert import convert
from pages.import_data import import_data
from pages.show_items import show_survey


def home_view(request: WSGIRequest):
    context = {}
    return render(request, template_name='pages/home.html', context=context)


def convert_view(request: WSGIRequest):
    context = convert()
    return render(request, template_name='pages/convert.html', context=context)


def import_data_view(request: WSGIRequest):
    context = import_data()
    return render(request, template_name='pages/import_data.html', context=context)


def incremental_import_view(request: WSGIRequest):
    context = incremental_import()
    return render(request, template_name='pages/incremental_import.html', context=context)


def show_survey_view(request: WSGIRequest):
    context = show_survey()
    return render(request, template_name='pages/show_survey.html', context=context)
