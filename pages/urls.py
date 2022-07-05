from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('complete_data/', views.complete_data_view, name='complete_data'),
    path('fill/', views.fill_view, name='fill'),
    path('import_data/', views.import_data_view, name='import_data'),
]
