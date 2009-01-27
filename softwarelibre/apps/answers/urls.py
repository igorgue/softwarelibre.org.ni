from django.conf.urls.default import *
import views

urlpatterns = patterns('',
        (r'^$', 'views.index'),
        (r'^pregunta/(?P<question_id>\d+)/$', 'views.view_question'),
        (r'^pregunta/nueva/$', 'views.ask_question'),
        (r'^pregunta/(?P<question_id>\d+)/responder$', 'views.answer_question'),
        )
