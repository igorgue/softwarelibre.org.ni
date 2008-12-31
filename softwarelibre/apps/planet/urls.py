from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^$', 'softwarelibre.apps.planet.views.index'),
     (r'^/autor/(?P<author>)/$', 'softwarelibre.apps.planet.views.filter_by_author')
     #(r'^/articulo/(?P<item>)/$', 'softwarelibre.apps.planet.views.show_item')
)
