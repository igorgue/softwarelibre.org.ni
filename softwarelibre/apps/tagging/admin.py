from django.contrib import admin
from apps.tagging.models import Tag, TaggedItem

admin.site.register(TaggedItem)
admin.site.register(Tag)
