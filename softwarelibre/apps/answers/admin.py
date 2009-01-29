from django.contrib import admin
from models import Question, Answer, Votes

admin.site.register(Question, 
        list_display = ['title', 'author'],
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

admin.site.register(Votes, 
        list_display = ['vote', 'author', 'answer'],
        list_filter = ['vote'],
        ordering = ['author', 'vote'],
        search_fields = ['author', 'question'],
        )
