from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import ReportForm
from .models import Event, Rsvp, User, GroupUser, Egroup, Report, ReportPhoto

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

	# create dictrionary of corresponding report for this event
	event_dictionary = {}
	# get Report Queryset
	reports = Report.objects.filter(eid__eid = id)

	rp_dictionary = {}
	for rp in reports:
		rppicture = ReportPhoto.objects.filter(rpid__rpid = rp.rpid)
		if rppicture :
			rp_dictionary[rp] = rppicture[0]
		else:
			rp_dictionary[rp] = None

	event_dictionary['report'] = rp_dictionary

	context = {'login': True, 'dbevent': dbevent, 'rsvp_set': rsvp_set, 'isRSVP': isRSVP, 'event_dictionary': event_dictionary}
	context['username'] = client

	return render(request, 'event/event_detail.html', context)

def report(request,id):

	context = {'login': False}
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))
	# get username login name
	client = request.session['username']

	# get event object
	dbevent = Event.objects.get(eid=id)

	# create dictrionary of corresponding report for this event
	event_dictionary = {}
	# get Report Queryset
	reports = Report.objects.filter(eid__eid = id)

	rp_dictionary = {}
	for rp in reports:
		rppicture = ReportPhoto.objects.filter(rpid__rpid = rp.rpid)
		if rppicture :
			rp_dictionary[rp] = rppicture[0]
		else:
			rp_dictionary[rp] = None

	event_dictionary['report'] = rp_dictionary

	# if the user POST report to event
	if request.method == "POST":

		# create a form instance and populate it with data from the request.
		form = ReportForm(request.POST, request.FILES)
		# if the form is valid, then do something
		if form.is_valid():
			print('report_post_valid')
			review_context = form.cleaned_data.get('report_text')

			# get current last rpid
			if Report.objects.all():
				last_rpid = Report.objects.all().latest('rpid')
			else :
				last_rpid = 0

			# construct the report model
			report = Report(uname = User.objects.get(uname=client), rdescription = review_context, eid = dbevent)
			# save to db
			report.save()

			# if user attach file, get the file and save to db
			if 'report_file' :
				report_file = form.cleaned_data.get('report_file')
				rpphoto = ReportPhoto(rpid = report, rp_photo = report_file)
				rpphoto.save()
				rpphoto.rp_photo_name = rpphoto.rp_photo.name
				rpphoto.save()
	context = {'login': True, 'dbevent': dbevent, 'event_dictionary':event_dictionary}

	return HttpResponseRedirect(reverse("event",kwargs={'id': id}))