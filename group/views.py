from django.shortcuts import render
from django.http import HttpResponse


def group_all(request):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'group/group_all.html', context)

def group(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'group/group.html', context)
