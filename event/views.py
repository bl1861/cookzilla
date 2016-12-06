from django.shortcuts import render
from django.http import HttpResponse

def event(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'event/event_detail.html', context)
