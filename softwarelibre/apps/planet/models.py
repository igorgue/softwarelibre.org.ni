from django.db import models
from django.contrib.auth.models import User 

from softwarelibre.apps.tag.models import Tag

class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'
        
    def __unicode__(self):
        return self.name

class Feed(models.Model):
    title = models.CharField(max_length = 500)
    feed_url = models.URLField(unique = True, max_length = 500)
    public_url = models.URLField(max_length = 500)
    is_active = models.BooleanField(default = True)

    def __unicode__(self):
        return self.title

class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length = 500)
    link = models.URLField(max_length = 500)
    summary = models.TextField(blank = True)
    date_modified = models.DateTimeField()
    guid = models.CharField(max_length = 500, unique = True, db_index = True)
    tags = models.ManyToManyField(Tag, verbose_name = 'Etiquetas')
#TODO: revisar esto....
    category = models.ManyToManyField(Category, verbose_name = 'Categoria')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ("-date_modified",)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.link

class Comment(models.Model):
    text = models.CharField('Comentario', max_length = 500)
    post = models.ForeignKey(FeedItem)
    author = models.ForeignKey(User)
