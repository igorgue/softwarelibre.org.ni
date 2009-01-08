from django.contrib import admin
from models import Tag

admin.site.register(Tag, 
        list_display = ['name'],
        search_fields = ['name'],
        )
