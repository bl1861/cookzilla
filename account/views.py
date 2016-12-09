from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from .models import User, Recipe, Egroup, Event, Rsvp, GroupUser, Review
from .forms import NewGroupForm, NewEventForm



# Abstract:
# Each function check if the username is in session, if not, redirect to login page.
# Each function put the 'account_item' in 'context' to show the title of the page
#

def profile(request):
	# if the user is not login, redirect to login page
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	# get username login name
	client= request.session['username']

	# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT * from _user where uname='"+client+"'")
	# list of tuples
	row = cursor.fetchone()

	dbuser = User.objects.get(uname = client)
	context = {'account_item': 'My Profile', 'login': True, 'dbuser':dbuser}

	return render(request, 'account/profile.html', context)


def groups(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'account_item': 'Groups', 'login': True, 'group_dict': {}}

	# get username login name
	client= request.session['username']

	# if this is a POST request, handle the input
	if request.method == "POST":
		form = NewGroupForm(request.POST)
		# if is valid ,create new group and save to database
		if form.is_valid():
			# get the input group name
			groupname = form.cleaned_data.get('groupname')
			# create new instance of egroup and save to db
			new_group = Egroup(gname=groupname)
			new_group.save()
			# create new instance of group_user and save to db
			join_group = GroupUser(uname=User.objects.get(uname=client),gid=new_group)
			join_group.save()
			print('create successfully !')

	'''# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT t3.gname from group_user as t1 inner join _user as t2 on t1.uname=t2.uname inner join egroup as t3 on t1.gid=t3.gid where t2.uname='"+client+"'")'''

	# create dictrionary for group and corresponding event
	group_event_rsvp_dict = {}
	# get GroupUser Queryset
	group_user = GroupUser.objects.filter(uname__uname = client)

	# iterate GroupUser Queryset
	for obj in group_user:
		# print(obj.gid.gname)
		# get Egroup object
		group_obj = obj.gid
		# get Event Queryset
		event_sets = Event.objects.filter(gid__gid = group_obj.gid)
		# create dictrionary for event and corresponding rsvp
		event_rsvp_dict = {}
		# iterate Event Queryset
		for event in event_sets:
			# check if rsvp
			rs = Rsvp.objects.filter(eid__eid = event.eid,uname__uname = client)
			print(rs)
			event_rsvp_dict[event] = rs

		group_event_rsvp_dict[group_obj] = event_rsvp_dict

	context['group_dict'] = group_event_rsvp_dict

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

	client= request.session['username']
	reviews = Review.objects.filter(uname=client)

	context = {'account_item': 'Reviews', 'login': True, 'reviews': reviews}
	return render(request, 'account/reviews.html', context)

def recipes(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	client= request.session['username']
	# get the recipe from this user
	recipe = Recipe.objects.filter(uname = client)
	context = {'account_item': 'Recipes', 'login': True , 'recipe':recipe}

	return render(request, 'account/recipes.html', context)


def new_event(request, id):
	print ("new_event gid = ", id)
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	context = {'account_item': 'Groups', 'login': True, 'group_dict': {}}
	# get username login name
	client= request.session['username']

	# if this is a POST request, handle the input
	if request.method == "POST":
		form = NewEventForm(request.POST)
		# if is valid ,create new group and save to database
		if form.is_valid():
			print('is_valid')
		else:
			print('not_valid')

	return HttpResponseRedirect(reverse("groups"))

