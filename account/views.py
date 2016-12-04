from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def profile(request):
	# if the user is not login, redirect to login page
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	# login is used to show login-layout
	context = {'login': True}
	return render(request, 'account/profile.html', context)


def groups(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'login': True}
	return render(request, 'account/groups.html', context)


def events(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'login': True}
	return render(request, 'account/events.html', context)


def rsvps(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'login': True}
	return render(request, 'account/RSVPs.html', context)

def reviews(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'login': True}
	return render(request, 'account/reviews.html', context)

