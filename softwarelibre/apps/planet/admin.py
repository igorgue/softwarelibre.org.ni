from django.contrib import admin
from models import Feed, FeedItem, Category, Comment

admin.site.register(Comment, 
        list_display = ['text', 'post', 'author'],
        list_filter = ['author', 'post'],
        ordering = ['post', 'author'],
        search_fields = ['author'],
        )

admin.site.register(Category, 
        list_display = ['name'],
        ordering = ['name'],
        )

admin.site.register(Feed, 
        list_display = ['title', 'slug', 'public_url', 'is_active'],
        list_filter = ['is_active'],
        ordering = ['title'],
        search_fields = ['title', 'public_url'],
        list_per_page = 500,
        prepopulated_fields = {'slug': ('title',)},
        )

admin.site.register(FeedItem, 
        list_display = ['title', 'feed', 'date_modified',],
        list_filter = ['feed'],
        search_fields = ['feed__title', 'feed__public_url'],
        #TODO: revisar esto!
        date_hierarchy = 'date_modified',
        )

