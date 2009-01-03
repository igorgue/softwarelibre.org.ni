from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from models import Feed, FeedItem, Tag

def index(request):
    planet_dict = {
            'items' : FeedItem.objects.select_related(),
            'paginate_by' : 15,
            }
    return render_to_response('planet/index.html', planet_dict)

def filter_by_author(request, author):
    try:
        feed = Feed.objects.get(title__iexact=author)
        post = FeedItem.objects.filter(feed = feed)
        return render_to_response('planet/author.html',
            {'author': feed, 'posts': post})
    except:
        raise Http404

def show_item(request, item):
    post = get_object_or_404(FeedItem, pk = item)
    return render_to_response('planet/item.html',
            { 'post': post})


def filter_by_tag(request, tag):
    try:
        #post = FeedItem.objects.filter(tags= Tag.objects.filter(name__iexact = tag))
        post = FeedItem.objects.filter(tags= tag)
        print post
        return render_to_response('planet/tag.html',
                {'tag': tag, 'posts': post})
    except:
        raise Http404

