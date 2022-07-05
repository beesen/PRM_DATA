from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from pages.complete_data import complete_data
from pages.fill import fill
from pages.import_data import import_data


def home_view(request: WSGIRequest):
    context = {}
    return render(request, template_name='pages/home.html', context=context)


def fill_view(request: WSGIRequest):
    context = fill()
    return render(request, template_name='pages/fill.html', context=context)


def import_data_view(request: WSGIRequest):
    context = import_data()
    return render(request, template_name='pages/import_data.html', context=context)


def complete_data_view(request: WSGIRequest):
    context = complete_data()
    return render(request, template_name='pages/complete_data.html', context=context)
