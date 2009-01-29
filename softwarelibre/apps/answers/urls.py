from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^$', 'softwarelibre.apps.answers.views.index'),
        (r'^pregunta/(?P<question_id>\d+)/$', 
            'softwarelibre.apps.answers.views.view_question'),
        (r'^pregunta/nueva/$', 'softwarelibre.apps.answers.views.ask_question'),
        (r'^pregunta/(?P<question_id>\d+)/responder$', 'softwarelibre.apps.answers.views.answer_question'),
        (r'^repuesta/(?P<answer_id>\d+)/vote_up$', 'softwarelibre.apps.answers.views.vote_up'),
        (r'^repuesta/(?P<answer_id>\d+)/vote_down$', 'softwarelibre.apps.answers.views.vote_down'),
        )
