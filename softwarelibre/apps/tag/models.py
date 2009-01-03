from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __unicode__(self):
        return self.name
