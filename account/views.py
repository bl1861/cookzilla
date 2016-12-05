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

	client= request.session['username']

	# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT * from _user where login_name='"+client+"'")
	# list of tuples
	row = cursor.fetchone()
	print(type(row[0]))

	context = {'uname':row[0],'login_name':row[1],'udescription':row[3]}
	'''for row in rows:
		context['groups'] = row[0]'''
	return render(request, 'account/profile.html', context)


def groups(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'login': True}
	return render(request, 'account/groups.html', context)


def events(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	cursor = connection.cursor()
	cursor.execute("SELECT event.eid, event.ename, event.etime FROM event")
	rows = cursor.fetchone()

	context = {'login': True, 'eid':str(rows[0]),'ename':rows[1],'etime':rows[2]}
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



