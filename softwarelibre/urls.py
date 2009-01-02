from django.conf.urls.defaults import *
from os import path as os_path
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Example:
    # (r'^softwarelibre/', include('softwarelibre.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #i (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
     (r'^cuentas/', include('apps.registration.urls')),
     (r'^planet/', include('apps.planet.urls')),
     (r'^planetfeed/', include('apps.feedjack.urls')),
     (r'^archivos/(.*)$', 'django.views.static.serve', {'document_root': os_path.join(settings.MEDIA_ROOT, '..', 'media')}),
)
