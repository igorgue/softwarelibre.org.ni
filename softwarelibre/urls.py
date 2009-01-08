from django.conf.urls.defaults import *
from os import path as os_path
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from apps.planet.feeds import PlanetFeed #, PlanetFeedTag, PlanetFeedAuthor
import settings

feeds = {
        'planet' : PlanetFeed,
        #'tag': PlanetFeedTag,
        #'author': PlanetFeedAuthor,
        }

urlpatterns = patterns('',
    # Example:
    # (r'^softwarelibre/', include('softwarelibre.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #i (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
     (r'^cuentas/', include('apps.registration.urls')),
     (r'^planeta/', include('apps.planet.urls')),
     (r'^perfiles/', include('apps.profiles.urls')),
     (r'^evento/', include('apps.events.urls')),
     (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
     #(r'^feeds/(p<url>.*)/(p<category>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
     (r'^archivos/(.*)$', 'django.views.static.serve', {'document_root': os_path.join(settings.MEDIA_ROOT, '..', 'media')}),
)
