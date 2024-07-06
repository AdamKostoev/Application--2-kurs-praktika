from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_vacancy', views.search_vacancy, name='search_vacancy'),
]
