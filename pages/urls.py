from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('incremental_import/', views.incremental_import_view, name='incremental_import'),
    path('convert/', views.convert_view, name='convert'),
    path('import_data/', views.import_data_view, name='import_data'),
    path('show_survey/', views.show_survey_view, name='show_survey'),
]
