from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RecipeForm

# Create your views here.
def recipe(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'recipe/recipe.html', context)


def new_recipe(request):
	# if the user is not login, redirect to login page
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	# if this is a POST request, we need to process the form data.
	if request.method == "POST":

		print (request.POST)
		# print (request.POST['tags'])
		# create a form instancee and populate it with data from the request.
		form = RecipeForm(request.POST)

		# if the form is valid, then do something

		if form.is_valid():
			print ("is_valid")
			# TODO: save the recipe here!
			# return HttpResponseRedirect(reverse("home"))

	context = {'login': True}
	return render(request, 'recipe/new_recipe.html', context)

