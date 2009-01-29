from django.db import models
from django.contrib.auth.models import User
from apps.tagging.fields import TagField

class Question(models.Model):
    title = models.CharField('Titulo', max_length = 100)
    text = models.TextField('Pregunta')
    author = models.ForeignKey(User, verbose_name='Usuario')
    correct_answer = models.ForeignKey('answers.Answer', blank = True, null = True, related_name = 'correct_answer')
    tags = TagField(verbose_name = 'Etiquetas', help_text = 'Ponga las etiquetas separadas por coma')    

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
    
    def __unicode__(self):
        return self.title

    @property
    def is_answered(self):
        if (self.correct_answer != null):
            return True
        else:
            return False

    def get_absolute_url(self):
        return '/soporte/pregunta/%d' % self.id


class Answer(models.Model):
    text = models.TextField('Repuesta')
    author = models.ForeignKey(User, verbose_name = 'Usuario')
    question = models.ForeignKey(Question, verbose_name = 'Pregunta')

    class Meta:
        verbose_name = 'Repuesta'
        verbose_name_plural = 'Repuestas'
    
    def __unicode__(self):
        return self.text
    
    @property
    def positive_votes(self):
        votes = Votes.objects.filter(answer = self, vote = 'Up')
        return len(votes)
    
    @property
    def negative_votes(self):
        votes = Votes.objects.filter(answer = self, vote = 'Down')
        return len(votes)

class Votes(models.Model):
    answer = models.ForeignKey(Answer, verbose_name = 'Repuesta')
    author = models.ForeignKey(User, verbose_name = 'Usuario')
    vote = models.CharField('Voto', max_length = 20,
            choices = (('Up', 'Up'),('Down', 'Down')))
    
    class Meta:
        verbose_name = 'Voto'
        verbose_name_plural = 'Votos'

    def __str__(self):
        return "%s - %s (%s)" % (self.answer, self.vote, self.author)
