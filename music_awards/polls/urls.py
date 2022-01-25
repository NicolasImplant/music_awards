from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
    path('<int:pk>/soyelmejor/', views.DetailView.as_view(), name='Detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='Results'),
    path('<int:question_id>/votes/', views.votes, name='Votes'),
]