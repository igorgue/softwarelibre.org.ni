from django.contrib import admin
from models import Question, Answer

admin.site.register(Question, 
        list_display = ['text', 'author'],
        list_filter = ['author'],
        ordering = ['author'],
        search_fields = ['author'],
        )

admin.site.register(Answer, 
        list_display = ['text', 'author', 'question'],
        list_filter = ['author', 'question'],
        ordering = ['author'],
        search_fields = ['author', 'question'],
        )
