from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^$', 'softwarelibre.apps.planet.views.index'),
     (r'^autor/(?P<author>[A-Za-z0-9]+(?:\+[A-Za-z0-9]+)*)/$', 'softwarelibre.apps.planet.views.filter_by_author'),
     (r'^articulo/(?P<item>[0-9]+)/$', 'softwarelibre.apps.planet.views.show_item'),
     (r'^(?P<tag>[A-Za-z0-9]+)/$', 'softwarelibre.apps.planet.views.filter_by_tag'),    
)
