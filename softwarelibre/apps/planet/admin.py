from django.contrib import admin
from models import Feed, FeedItem, Tag

admin.site.register(Tag, 
        list_display = ['name'],
        ordering = ['name'],
        )

admin.site.register(Feed, 
        list_display = ['title', 'public_url', 'is_active'],
        list_filter = ['is_active'],
        ordering = ['title'],
        search_fields = ['title', 'public_url'],
        list_per_page = 500,
        )

admin.site.register(FeedItem, 
        list_display = ['title', 'feed', 'date_modified'],
        list_filter = ['feed'],
        search_fields = ['feed__title', 'feed__public_url'],
        #TODO: revisar esto!
        #date_hierarchy = ['date_modified'],
        )

