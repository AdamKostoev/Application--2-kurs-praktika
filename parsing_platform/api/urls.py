from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_vacancies', views.all_vacancies, name='all_vacancies'),
]