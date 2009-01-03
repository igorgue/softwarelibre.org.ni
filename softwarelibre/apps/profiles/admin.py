from django.contrib import admin
from models import Profile

admin.site.register(Profile, 
        list_display = ['user', 'website', 'avatar'],
        ordering = ['user'],
        search_fields = ['user'],
        )
