from django.shortcuts import render
from django.http import HttpResponse

def event_all(request):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'event/event_all.html', context)


def event(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'event/event.html', context)
