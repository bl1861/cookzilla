from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from django.core import serializers
from .models import Event
import json

def profile(request):
	# if the user is not login, redirect to login page
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))
	# query from db
	# cursor = connection.cursor()
	# cursor.execute("SELECT group_user.uname from _user inner join group_user on _user.uname = group_user.uname where _user.uname = 'Rubby'")
	# rows = cursor.fetchall()
	# print(rows)
	# data = serializers.serialize("json", Event.objects.all())
	# context = {'groups':rows}
	#for row in rows:
	#	context['groups'].append(row)
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
	cursor = connection.cursor()
	cursor.execute("SELECT event.eid, event.ename, event.etime FROM event")
	rows = cursor.fetchone()

	passin = {'eid':str(rows[0]),'ename':rows[1],'etime':rows[2]}
	return render(request, 'account/events.html', passin)


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



