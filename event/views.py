from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Event, Rsvp, User, GroupUser, Egroup

def event(request, id):
	context = {'login': False}
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))	
	# get username login name
	client = request.session['username']

	# get event object
	dbevent = Event.objects.get(eid=id)

	# if the user POST to event
	if request.method == "POST": 

		dbUser = User.objects.get(uname=client)
		dbGroup = Egroup.objects.get(gid=dbevent.gid.gid)
		dbGroupUser = GroupUser.objects.filter(uname__uname=dbUser.uname, gid__gid=dbGroup.gid)
		# If the user dose not join the group, join the group first
		if not dbGroupUser:
			join_group = GroupUser(uname=dbUser, gid=dbGroup)
			join_group.save()
			print ("Join Group Successfully!")

		rsvp_event = Rsvp(eid=dbevent, uname=dbUser)
		rsvp_event.save()
		print ("RSVP Successfully!")

	# get rsvp set
	rsvp_set = Rsvp.objects.filter(eid__eid=id)

	# check if the user RSVP the event
	isRSVP = Rsvp.objects.filter(eid__eid=id, uname__uname=client)

	context = {'login': True, 'dbevent': dbevent, 'rsvp_set': rsvp_set, 'isRSVP': isRSVP}
	context['username'] = client
	
	return render(request, 'event/event_detail.html', context)
