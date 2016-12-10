from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User, GroupUser, Event, Egroup, Rsvp



def group_all(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	# get username login name
	client = request.session['username']

	context = {'account_item': 'Groups', 'login': True, 'group_dict': {}}
	context['username'] = client

	'''# query from db
	cursor = connection.cursor()
	cursor.execute("SELECT t3.gname from group_user as t1 inner join _user as t2 on t1.uname=t2.uname inner join egroup as t3 on t1.gid=t3.gid where t2.uname='"+client+"'")'''


	# create dictrionary for group and corresponding event
	group_event_rsvp_dict = {}
	# get Egropu Queryset
	group_all = Egroup.objects.all()
	# get GroupUser Queryset
	group_user = GroupUser.objects.filter(uname__uname = client)

	# iterate GroupUser Queryset
	for group_obj in group_all:
		# print(obj.gname)
		# get Egroup object
		# group_obj = obj.gid
		# get Event Queryset
		group_joined = False
		for obj in group_user:
			g_obj = obj.gid
			if group_obj.gid == g_obj.gid:
				group_joined = True
				break

		event_sets = Event.objects.filter(gid__gid = group_obj.gid)
		# create dictrionary for event and corresponding rsvp
		group_detail = {'joined': group_joined}

		event_rsvp_dict = {}
		# iterate Event Queryset
		for event in event_sets:
			# check if rsvp
			rs = Rsvp.objects.filter(eid__eid = event.eid,uname__uname = client)
			print(rs)
			event_rsvp_dict[event] = rs

		group_detail['group_detail'] = event_rsvp_dict
		group_event_rsvp_dict[group_obj] = group_detail

	context['group_dict'] = group_event_rsvp_dict

	return render(request, 'group/group_all.html', context)

def join_group(request, id):
		
	if request.method == "POST":
		if 'username' in request.session:
			client = request.session['username']
			join_group = GroupUser(uname=User.objects.get(uname=client),gid=Egroup.objects.get(gid=id))
			join_group.save()
			print('join group successfully !')
		else:
			HttpResponseRedirect(reverse('login'))

	return HttpResponseRedirect(reverse('group_all'))



### This is old version of group_all
# def group_all(request):
# 	context = {'login': False}
# 	if 'username' in request.session:
# 		context['login'] = True
# 	return render(request, 'group/group_all.html', context)









