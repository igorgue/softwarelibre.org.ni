from django.core.Paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from models import Question, Answer, Vote
from forms import QuestionForm, AnswerForm

def index(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list, 40)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        questions = paginator(page)
    except (EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render_to_response('answers/view_question.html', questions)

def view_question(request, question_id):
    question = get_object_or_404(Question, id = id)
    answers_list = question.answer_set.all()
    paginator = Paginator(answers_list, 20)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        raise Http404

    try:
        answers = paginator(page)
    except (EmptyPage, InvalidPage):
        answers = paginator.page(paginator.num_pages)

    form = AnswerForm()
    dict = {'question': question, 'answers': answers, 'form': form}
    return render_to_response('answers/view_question.html', dict)

def ask_question(request):
    if request.method == POST:
        pass
    else:
        form = QuestionForm()
        return render_to_response('answers/ask_question.html', form)

def answer_question(request, question_id):
    if request.method == POST:
        #TODO: process form
        pass
    url = '/soporte/pregunta/' + question_id 
    return HttpResponseRedirect(url)
