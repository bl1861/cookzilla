from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.urls import reverse
from db.models import User,Conversion,Rsvp,Egroup,Event,GroupUser,Ingredient,Photo,Recipe,Related,Report,ReportPhoto,Review,ReviewPhoto,Tag


def home(request):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
		context['username'] = request.session['username']
		return render(request, 'main/home.html', context);

	return render(request, 'main/home.html')


def login(request):

	# if this is a POST request, we need to process the form data.
	if request.method == "POST":

		# create a form instancee and populate it with data from the request.
		form = UserForm(request.POST)

		# if the form is valid, then do something
		if form.is_valid():

			user = form.cleaned_data.get('username')
			pw = form.cleaned_data.get('password')
			dbuser = User.objects.filter(login_name = user,password=pw)

			if dbuser:
				print(form.cleaned_data.get('username'))
				print(form.cleaned_data.get('password'))
				request.session['username'] = form.cleaned_data.get('username')
				return HttpResponseRedirect(reverse("home"))

	return render(request, 'main/login.html')


def logout(request):
	if 'username' in request.session:
		request.session.pop('username')

	return render(request, 'main/logout.html')

