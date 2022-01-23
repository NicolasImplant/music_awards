from unicodedata import name
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='Index'),
    path('<int:question_id>/soyelmejor/', views.detail, name='Detail'),
    path('<int:question_id>/results/', views.results, name='Results'),
    path('<int:question_id>/votes/', views.votes, name='Votes'),
]