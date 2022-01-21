from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Estas en la página principal de music awards')


def detail(request, question_id):
    return HttpResponse(f'Estas viendo la pregunta número {question_id}')


def results(request, question_id):
    return HttpResponse(f'Estas viendo los resultados de la pregunta número {question_id}')


def votes(request, question_id):
    return HttpResponse(f'Estas votando a la pregunta número {question_id}')