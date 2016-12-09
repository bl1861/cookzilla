from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RecipeForm
from django.urls import reverse
from .models import User, Recipe, Egroup, Event, Rsvp, Tag, Review, Ingredient

# Create your views here.
def recipe(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True

	#client= request.session['username']

	# create dictrionary of corresponding review & ingredient for thos recipe
	recipe_dictionary = {}

	# get Recipe
	recipe = Recipe.objects.filter(rid = id)
	recipe_dictionary['recipe'] = recipe

	# get Review Queryset
	reviews = Review.objects.filter(rid__rid = id)
	recipe_dictionary['review'] = reviews

	# get Ingredient Queryset
	ingredients = Ingredient.objects.filter(rid__rid = id)
	recipe_dictionary['ingredient'] = ingredients

	# get Tag Queryset
	tags = Tag.objects.filter(rid__rid = id)

	# dictionary to store key:tag model / value: recipe list
	relate_dictionary = {}

	for tag in tags :
		recipe_set = Recipe.objects.raw("SELECT r.rid from recipe as r inner join tag as t on r.rid=t.rid WHERE t.tname='"+tag.tname+"' and r.rid !="+id+"" )
		print("t:"+tag.tname)

		# list to store related recipe model
		related = []
		for relate in recipe_set :
			print(relate.rtitle)
			related.append(relate)

		relate_dictionary[tag] = related

	recipe_dictionary['relate'] = relate_dictionary
	context = {'account_item': 'Recipes', 'login': True , 'recipe_dictionary': recipe_dictionary}
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

