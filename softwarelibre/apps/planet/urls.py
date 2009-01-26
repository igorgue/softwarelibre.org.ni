from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^$', 'softwarelibre.apps.planet.views.index'),
     (r'^autor/(?P<author>.*)/$', 'softwarelibre.apps.planet.views.filter_by_author'),
     (r'^articulo/(?P<item>\d+)/$', 'softwarelibre.apps.planet.views.show_item'),
     (r'^(?P<category>.*)/$', 'softwarelibre.apps.planet.views.filter_by_category'),    
)
