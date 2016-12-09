from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Rsvp

def event(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True

	# list of tuples
	dbevent = Event.objects.get(eid=id)

	# get rsvp set
	rsvp_set = Rsvp.objects.filter(eid__eid=id)

	context = {'login': True, 'dbevent': dbevent, 'rsvp_set': rsvp_set}
	return render(request, 'event/event_detail.html', context)
