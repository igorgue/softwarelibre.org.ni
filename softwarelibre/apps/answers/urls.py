from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^$', 'softwarelibre.apps.answers.views.index'),
        (r'^pregunta/(?P<question_id>\d+)/$', 
            'softwarelibre.apps.answers.views.view_question'),
        (r'^pregunta/nueva/$', 'softwarelibre.apps.answers.views.ask_question'),
        (r'^pregunta/(?P<question_id>\d+)/responder$', 'softwarelibre.apps.answers.views.answer_question'),
        )
