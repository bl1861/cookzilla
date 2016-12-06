from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from .models import User



# Abstract:
# Each function check if the username is in session, if not, redirect to login page.
# Each function put the 'account_item' in 'context' to show the title of the page
#

def profile(request):
	# if the user is not login, redirect to login page
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	#get username login name
	client= request.session['username']

	# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT * from _user where uname='"+client+"'")
	# list of tuples
	row = cursor.fetchone()

	dbuser = User.objects.get(uname = client)

	#context = {'account_item': 'My Profile', 'login': True, 'uname':row[0],'login_name':row[1],'udescription':row[3],'ufile':row[4]}
	context = {'account_item': 'My Profile', 'login': True, 'dbuser':dbuser}

	return render(request, 'account/profile.html', context)


def groups(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'account_item': 'Groups', 'login': True, 'gname': []}

	#get username login name
	client= request.session['username']

	# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT t3.gname from group_user as t1 inner join _user as t2 on t1.uname=t2.uname inner join egroup as t3 on t1.gid=t3.gid where t2.uname='"+client+"'")

	# iterate of gname
	rows = cursor.fetchall()
	for row in rows:
		context['gname'].append(row[0])

	return render(request, 'account/groups.html', context)


def events(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'account_item': 'Events', 'login': True, 'event': []}
	client= request.session['username']

	# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT e.ename from (SELECT t3.gid from group_user as t1 inner join _user as t2 on t1.uname=t2.uname inner join egroup as t3 on t1.gid=t3.gid where t2.uname='"+client+"') as g inner join event as e on g.gid=e.gid")

	# iterate of event
	rows = cursor.fetchall()

	for row in rows:
		context['event'].append(row[0])

	return render(request, 'account/events.html', context)


def rsvps(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'account_item': 'Events', 'login': True, 'ename': []}
	client= request.session['username']

	# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT distinct e.ename from _user as u inner join rsvp as r on u.uname=r.uname inner join event as e on r.eid=e.eid WHERE u.uname='"+client+"'")

	# iterate of ename
	rows = cursor.fetchall()
	for row in rows:
		context['ename'].append(row[0])


	return render(request, 'account/RSVPs.html', context)

def reviews(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'account_item': 'Reviews', 'login': True}
	return render(request, 'account/reviews.html', context)

def recipes(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'account_item': 'Recipes', 'login': True}
	return render(request, 'account/recipes.html', context)





