from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    website = models.URLField()
    avatar = models.ImageField(upload_to = 'img/profile-pics', 
            height_field='50', width_field='50')
    user = models.ForeignKey(User, unique = True)
    karma = models.IntegerField(default = 0)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    class Admin:
        pass

    def __unicode__(self):
        return self.user.username
