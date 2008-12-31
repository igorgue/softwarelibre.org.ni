from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from models import Feed, FeedItem

def index(request):
    planet_dict = {
            'items' : FeedItem.objects.select_related(),
            'paginate_by' : 15,
            }
    return render_to_response('planet/index.html', planet_dict)

def filter_by_author(request, author):
    pass

def show_item(request, item):
    pass
