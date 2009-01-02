from django.contrib.syndication.feeds impor Feed
from models import FeedItem

class PlanetFeed(Feed):
    title = "Planeta del Grupo de Usario de GNU/Linux Nicaragua"
    link = "http://sofwarelibre.org.ni/planet" #TODO: revisar el link al feed
    description = "Articulos agregados de la comunidad GNU/Linux de Nicaragua"

    def items(self):
        return FeedItem.objects.all()[:10]
