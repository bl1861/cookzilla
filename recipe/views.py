from django.shortcuts import render
from django.http import HttpResponseRedirect

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

	context = {'login': True}
	return render(request, 'recipe/new_recipe.html', context)

