import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    """Modelo de pregunta"""
    question_text  = models.CharField(max_length = 200)
    pub_date       = models.DateTimeField("Date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)  

    

class Choice(models.Model):
    """Modelo de opcion de respuesta"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choise_text
