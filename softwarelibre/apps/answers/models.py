from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField('Pregunta', max_length = 500)
    author = models.ForeignKey(User)
    
    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
    
    def __unicode__(self):
        return self.text 


class Answer(models.Model):
    text = models.CharField('Repuesta', max_length = 500)
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)

    class Meta:
        verbose_name = 'Repuesta'
        verbose_name_plural = 'Repuestas'
    
    def __unicode__(self):
        return self.text
