from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from models import Question, Answer, Votes
from forms import QuestionForm, AnswerForm
from apps.tagging.models import TaggedItem, Tag

def index(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list, 40)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        questions = paginator.page(page)
    except (EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render_to_response('answers/answers_index.html',
            {'questions': questions})

def view_question(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    answers_list = question.answer_set.all()
    paginator = Paginator(answers_list, 20)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        raise Http404

    try:
        answers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        answers = paginator.page(paginator.num_pages)
    
    if request.user.is_authenticated():
        form = AnswerForm()
    else:
        form = None

    dict = {'question': question, 'answers': answers, 'form': form}
    return render_to_response('answers/view_question.html', dict)

def ask_question(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                text = form.cleaned_data['question']
                tags = form.cleaned_data['tags']
                author = request.user
                question = Question(title = title, text = text, 
                        tags = tags, author = author)
                question.save()
                return view_question(request, question.id)
             #else:
               # pass #TODO: validar cuando el formulario de errores.
        else:
            form = QuestionForm()
            return render_to_response('answers/ask_question.html', {'form': form})
    else:
        return HttpResponseRedirect('cuentas/login')

def answer_question(request, question_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                question = Question.objects.get(id = question_id)
                author = request.user
                text = form.cleaned_data['answer']
                answer = Answer(text = text, author = author,
                        question = question)
                answer.save()
                return  view_question(request, question_id)
            else:
                pass #TODO: validar cuando el formulario de errores.
    else:
        return HttpResponseRedirect('/cuentas/login')

def vote_up(request, answer_id):
    if request.user.is_authenticated():
        answer = Answer.objects.get(id = answer_id)
        votos = Votes.objects.filter(author = request.user, answer = answer)
        question_id = answer.question.id       
        if len(votos) == 0:
            voto = Votes(answer = answer, author = request.user, vote = 'Up')
            voto.save()
        else:
            pass #TODO mandar un mensaje de que ya voto.
            #request.session['message'] = 'Usted ya ha votado por esta repuesta.' 
        return HttpResponseRedirect('/soporte/pregunta/' + str(question_id))
    else:
        return HttpResponseRedirect('/cuentas/login')

def vote_down(request, answer_id):
    if request.user.is_authenticated():
        answer = Answer.objects.get(id = answer_id)
        question_id = answer.question.id       
        votos = Votes.objects.filter(author = request.user, answer = answer)
        if len(votos) == 0:
            voto = Votes(answer = answer, author = request.user, vote = 'Down')
            voto.save()
        else:
            pass #TODO mandar un mensaje de que ya voto.
            #request.session['message'] = 'Usted ya ha votado por esta repuesta.' 
        return HttpResponseRedirect('/soporte/pregunta/' + str(question_id))
    else:
        return HttpResponseRedirect('/cuentas/login')

def filter_question_by_tag(request, tag):
    selected_tag = get_object_or_404(Tag, name = tag)
    question_list = TaggedItem.objects.get_by_model(Question, selected_tag)
    paginator = Paginator(question_list, 40)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        questions = paginator.page(page)
    except (EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render_to_response('answers/filter_by_tag.html',
            {'questions': questions})
