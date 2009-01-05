from django.contrib import admin

from events.models import *

class EventCategoryAdmin(admin.ModelAdmin):
	list_display = ['name',]
	
	def queryset(self, request):
		return EventCategory.on_site.all()
	
	def save_model(self, request, obj, form, change):
		obj.save()
		from django.contrib.sites.models import Site
		current_site = Site.objects.get_current()
		if current_site not in obj.sites.all():
			obj.sites.add(current_site)

admin.site.register(EventCategory, EventCategoryAdmin)


class EventAdmin(admin.ModelAdmin):
	list_display = ['name', 'start', 'category_list']
	list_filter = ['start', 'categories',]
	search_fields = ['name', 'description', 'location']
	date_hierarchy = 'start'
	filter_horizontal = ['categories']
	fieldsets = (
		('Event info',{
			'fields': ('name', 'start', 'description'),
		}),
		('More options...',{
			'classes': ['collapse'],
			'fields': ('location', 'time', 'end', 'categories'),
		}),
	)
	
	def queryset(self, request):
		return Event.on_site.all()
	
	def save_model(self, request, obj, form, change):
		obj.save()
		from django.contrib.sites.models import Site
		current_site = Site.objects.get_current()
		if current_site not in obj.sites.all():
			obj.sites.add(current_site)
	
admin.site.register(Event, EventAdmin)