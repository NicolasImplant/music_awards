from django.db import models

class Question(models.Model):
    """Modelo de pregunta"""
    question_text  = models.CharField(max_length = 200)
    pub_date       = models.DateTimeField("Date published")
    

class Choices(models.Model):
    """Modelo de opcion de respuesta"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
