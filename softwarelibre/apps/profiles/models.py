from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    website = models.URLField()
    avatar = models.ImageField(upload_to = 'img/profile-pics', 
            height_field='50', width_field='50')
    user = models.ForeignKey(User, unique = True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
