from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.urls import reverse


def home(request):
	# render will go to 'templates' folder, and look for 'home/home.html'
	# notice: we should create 'home' folder in current folder. It avoids filename collision
	return render(request, 'main/home.html')


def login(request):

	# if this is a POST request, we need to process the form data.
	if request.method == "POST":

		# create a form instancee and populate it with data from the request.
		form = UserForm(request.POST)

		# if the form is valid, then do something
		if form.is_valid():
			print(form.cleaned_data.get('username'))
			print(form.cleaned_data.get('password'))
			request.session['username'] = form.cleaned_data.get('username')
			return HttpResponseRedirect(reverse("home"))

	return render(request, 'main/login.html')
	# return HttpResponse("<h2>HEY! This is Login page.</h2>")



def logout(request):
	if 'username' in request.session:
		request.session.pop('username')

	return render(request, 'main/logout.html')
