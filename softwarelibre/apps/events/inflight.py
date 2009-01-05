INFLIGHT_APP_LABEL = 'events'
TAB_TEXT = "Events"
TAB_URL = '/inflight/events/'
ADMIN_REQUIRED = False

from django.template.defaultfilters import truncatewords_html, striptags
from events.models import Event

class SearchableEvent(object):	
	def get_results(self, keywords):
		results = []
		for event in Event.on_site.upcoming():
			title_score = event.name.lower().count(keywords) * 5 # Name has five times the relevance of description
			desc_score = event.description.lower().count(keywords)
			total_score = title_score + desc_score
			snippet = event.description
			if total_score > 0:
				import textile
				snippet = truncatewords_html(textile.textile(snippet.encode('ascii','xmlcharrefreplace')), 25)
				results.append((event, event.name, snippet, total_score))
		return results