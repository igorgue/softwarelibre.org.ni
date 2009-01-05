from django.conf.urls.defaults import *
from events.models import Event

event_dict = {
	'queryset': Event.on_site.all(),
	'template_object_name': 'event'
}

urlpatterns = patterns('django.views.generic',
	url(r'^event-(?P<object_id>\d+)/$', 'list_detail.object_detail', event_dict, name="event-detail"),
	url(r'^(?P<year>\d{4})/$','date_based.archive_year', dict(event_dict, allow_future=True, date_field='start', allow_empty=True, make_object_list=True)),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','date_based.archive_month', dict(event_dict, allow_future=True, date_field='start', allow_empty=True)),
)
