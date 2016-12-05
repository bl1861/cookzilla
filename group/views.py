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

def new_group(request):
	# if the user is not login, redirect to login page
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'login': True}
	return render(request, 'group/new_group.html', context)


