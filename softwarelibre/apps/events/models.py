from datetime import date, timedelta
from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.template.defaultfilters import date as datefilter
from django.conf import settings

class EventCategory(models.Model):

	objects = models.Manager()
	on_site = CurrentSiteManager(field_name='sites')
	name = models.CharField('Nombre', max_length=100)
	sites = models.ManyToManyField(Site)
	
	def site_list(self):
		return self.sites.all()
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name_plural = u'Categorias de eventos'
		verbose_name = u'Categoria de evento'

		
class EventManager(CurrentSiteManager):	

	def upcoming(self, days=None):
		"""
		Returns all Events with a start date in the next ``days`` days.
		If ``days`` is None, get all upcoming events.
		Resulting QuerySet is ordered with the soonest event first.
		TODO: Should also get "in progress" events (ones that have started but not ended).
		"""
		now = date.today()
		if days is None:
			return self.get_query_set().filter(
				((models.Q(end__isnull=True) | models.Q(end__gte=now)) & models.Q(start__gte=now)) |
				(models.Q(start__lte=now) & models.Q(end__gte=now))
			).order_by('start')
		else:
			return self.get_query_set().filter(
				(models.Q(end__isnull=True) & models.Q(start__range=(now, now + timedelta(days=int(days))))) |
				(models.Q(end__isnull=False) & models.Q(start__range=(now, now + timedelta(days=int(days)))) & models.Q(end__gte=now))
			).order_by('start')
		
	def past(self):
		"""
		Gets all the Events that have passed.
		Queryset is ordered with the most recently past event first.
		"""
		# Because end dates can be blank, we need to check for Events
		# with an end date in the past OR Events with start dates in the
		# past and no end dates.
		now = date.today()
		return self.get_query_set().filter(models.Q(end__lt=now) | models.Q(end__isnull=True), start__lt=now)
		

def format(d):
	if d.year == date.today().year:
		s = "F j"
	else:
		s = "F j, Y"
	return mark_safe(datefilter(d, s))

def isValidEndDate(field_data, all_data):
	" Validates that end date is less than (after) the start date. "
	if field_data:
		if  date(*[int(v) for v in field_data.split('-')]) <=  date(*[int(v) for v in all_data['start'].split('-')]):
			raise ValidationError("The end date must be after the start date.  Please select a new end date, or leave blank if this event is only one day long.")

class Event(models.Model):
	objects = models.Manager()
	on_site = EventManager(field_name='sites')
	
	name = models.CharField(max_length=250, help_text=u'Example: "Concierto de Wendy Sulca y Yahari"')
	description = models.TextField('Descripcion', blank=True,
		help_text=u'* Opcional.')
	location = models.TextField('Lugar', blank=True, help_text=u"* Opcional.")
	start = models.DateField(u"Fecha",
            help_text=u'Formato: yyyy-mm-dd. '
		'Si el evento tarda mas de un dia ingrese la fecha de incio y luego la de fin en el campo de abajo.')
	time = models.CharField('Hora', blank=True, max_length=100, help_text=u'* Opcional.  Ejemplos: "8 am - 4 pm", "7:30 pm"')
	# Todo -- continue to validate that the end is after the start?
	end = models.DateField(u'Fecha Final', blank=True, null=True,
		help_text=u'* Optional. Si el evento tarda mas de un dia si no dejar en blanco.')
	categories = models.ManyToManyField(EventCategory, blank=True, null=True, limit_choices_to={'sites__id': settings.SITE_ID})
	sites = models.ManyToManyField(Site, editable=False, default=[settings.SITE_ID])
	
	def __unicode__(self):
		return self.name
		
	# @models.permalink
	def get_absolute_url(self):
		return u'/evento/%s/' % self.id
		
	def has_passed(self):
		if self.end:
			return self.end < date.today()
		else:
			return self.start < date.today()
	
	def category_list(self):
		if self.categories.all():
			return ", ".join([ c.name for c in self.categories.all() ])
		return '(No hay categorias)'
		
	def site_list(self):
		return self.sites.all()
		
	def is_mutiple_days(self):
		return self.end is not None and self.end > self.start
		
	def get_next_upcoming(self):
		try:
			return Event.on_site.upcoming().filter(start__gte=self.start).exclude(id=self.id)[0]
		except IndexError:
			return None
			
	def get_previous_upcoming(self):
		try:
			return Event.on_site.upcoming().filter(start__lte=self.start).exclude(id=self.id)[0]
		except IndexError:
			return None
		
	def date_span(self):
		if self.end:
			s = "%s &mdash; %s" % (format(self.start), format(self.end))
		else:
			s = format(self.start)
		return mark_safe(s)
	date_span.short_description = 'date'
	date_span.admin_order_field = 'start'
	date_span.allow_tags = True

    #class Meta:
    #    verbose_name_plural = u'Eventos'
    #   verbose_name = u'Evento'

