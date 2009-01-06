from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from models import Feed, FeedItem, Category
from softwarelibre.apps.tag.models import Tag

def index(request):
    planet_dict = {
            'items' : FeedItem.objects.select_related(),
            'paginate_by' : 15,
            }
    return render_to_response('planet/index.html', planet_dict)

def filter_by_author(request, author):
    try:
        feed = Feed.objects.get(slug = author)
        post = FeedItem.objects.filter(feed = feed)
        return render_to_response('planet/author.html',
                {'author': feed, 'posts': post}) #WTF is happening here?????
    except:
        raise Http404

def show_item(request, item):
    post = get_object_or_404(FeedItem, pk = item)
    return render_to_response('planet/item.html',
            { 'post': post})


def filter_by_category(request, category):
    try:
        selected_category = Category.objects.get(name__iexact = category)
        posts = selected_category.feeditem_set.all()
        return render_to_response('planet/category.html',
                {'category': selected_category, 'posts': posts})
    except:
        raise Http404

def filter_by_tag(request, tag):
    try:
        selected_tag = Tag.objects.get(name__iexact = tag)
        posts = selected_tag.feeditem_set.all()
        return render_to_response('planet/tag.html',
                {'tag': selected_tag, 'posts': posts})
    except:
        raise Http404
