"""
>>> import datetime
>>> from events.models import Event
>>> from django.contrib.sites.models import Site
>>> SITE = Site.objects.get_current()

>>> TOMORROW = datetime.datetime.now() + datetime.timedelta(days=1)
>>> FUTURE_15_DAYS = datetime.datetime.now() + datetime.timedelta(days=15)
>>> FUTURE_30_DAYS = datetime.datetime.now() + datetime.timedelta(days=30)
>>> FUTURE_90_DAYS = datetime.datetime.now() + datetime.timedelta(days=90)

>>> YESTERDAY = datetime.datetime.now() + datetime.timedelta(days=-1)
>>> PAST_15_DAYS = datetime.datetime.now() + datetime.timedelta(days=-15)
>>> PAST_30_DAYS = datetime.datetime.now() + datetime.timedelta(days=-30)
>>> PAST_90_DAYS = datetime.datetime.now() + datetime.timedelta(days=-90)

>>> Event.on_site.upcoming()
[]

# Create an Event that starts tomorrow.  Should be in upcoming.
>>> event1 = Event(name="My Birthday tomorrow", location="The bowling alley", start=TOMORROW)
>>> event1.save()
>>> event1.sites.add(SITE)
>>> Event.on_site.upcoming()
[<Event: My Birthday tomorrow>]

# Create an Event that has passed.  Should NOT be in upcoming.
>>> woodstock = Event(name="Woodstock", start=datetime.datetime(1969, 8, 18))
>>> woodstock.save()
>>> woodstock.sites.add(SITE)
>>> Event.on_site.upcoming()
[<Event: My Birthday tomorrow>]

# Create some events at different intevals in the future.
>>> future_15 = Event(name="15 days from now", start=FUTURE_15_DAYS)
>>> future_15.save()
>>> future_15.sites.add(SITE)
>>> future_90 = Event(name="90 days from now", start=FUTURE_90_DAYS)
>>> future_90.save()
>>> future_90.sites.add(SITE)
>>> future_30 = Event(name="30 days from now", start=FUTURE_30_DAYS)
>>> future_30.save()
>>> future_30.sites.add(SITE)

# Events should be ordered with soonest Event first.
>>> Event.on_site.upcoming()
[<Event: My Birthday tomorrow>, <Event: 15 days from now>, <Event: 30 days from now>, <Event: 90 days from now>]

# Should be able to specify how many days in the future
# to look for upcoming events.
>>> Event.on_site.upcoming(90)
[<Event: My Birthday tomorrow>, <Event: 15 days from now>, <Event: 30 days from now>, <Event: 90 days from now>]
>>> Event.on_site.upcoming(30)
[<Event: My Birthday tomorrow>, <Event: 15 days from now>, <Event: 30 days from now>]
>>> Event.on_site.upcoming(45)
[<Event: My Birthday tomorrow>, <Event: 15 days from now>, <Event: 30 days from now>]
>>> Event.on_site.upcoming(30)
[<Event: My Birthday tomorrow>, <Event: 15 days from now>, <Event: 30 days from now>]
>>> Event.on_site.upcoming(15)
[<Event: My Birthday tomorrow>, <Event: 15 days from now>]
>>> Event.on_site.upcoming(10)
[<Event: My Birthday tomorrow>]

# Create some events in the past.
>>> yesterday = Event(name="Something that happened yesterday", start=YESTERDAY)
>>> yesterday.save()
>>> yesterday.sites.add(SITE)
>>> past_15 = Event(name="15 days ago", start=PAST_15_DAYS)
>>> past_15.save()
>>> past_15.sites.add(SITE)
>>> past_90 = Event(name="90 days ago", start=PAST_90_DAYS)
>>> past_90.save()
>>> past_90.sites.add(SITE)
>>> past_30 = Event(name="30 days ago", start=PAST_30_DAYS)
>>> past_30.save()
>>> past_30.sites.add(SITE)

# None of the past events should be upcoming.
>>> Event.on_site.upcoming()
[<Event: My Birthday tomorrow>, <Event: 15 days from now>, <Event: 30 days from now>, <Event: 90 days from now>]

All the past events should be shown, with the most recent first.
>>> Event.on_site.past()
[<Event: Something that happened yesterday>, <Event: 15 days ago>, <Event: 30 days ago>, <Event: 90 days ago>, <Event: Woodstock>]

"""