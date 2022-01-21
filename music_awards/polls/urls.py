from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('<int:question_id>', views.detail, name='Detail'),
    path('<int:question_id>/results/', views.results, name='Results'),
    path('<int:question_id>/votes/', views.votes, name='Votes'),
]