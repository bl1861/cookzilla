from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RecipeForm
from django.urls import reverse
from .models import User, Recipe, Egroup, Event, Rsvp, Tag, Review, Ingredient
import datetime

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
		# get username login name
		client= request.session['username']


		# print (request.POST['tags'])
		# create a form instancee and populate it with data from the request.
		form = RecipeForm(request.POST, request.FILES)
		print (request.FILES)

		# if the form is valid, then do something

		if form.is_valid():

			# TODO: save the recipe here!
			recipe_title = form.cleaned_data.get('recipe_title')
			recipe_content = form.cleaned_data.get('recipe_content')
			recipe_servings = form.cleaned_data.get('recipe_servings')
			iname1 = form.cleaned_data.get('iname1')
			quantity1 = form.cleaned_data.get('quantity1')
			unit1 = form.cleaned_data.get('unit1')

			# get current last rid
			last_rid = Recipe.objects.all().latest('rid')
			# construct a new created recipe
			recipe = Recipe(rid = last_rid.rid+1 , rtitle = recipe_title, rcontent = recipe_content, rserving = recipe_servings, uname = User.objects.get(uname=client), rtime = datetime.datetime.now())

			if 'recipe_photo':
				recipe_photo = form.cleaned_data['recipe_photo']
				recipe.rphoto = recipe_photo

			# save recipe object to db
			recipe.save()
			print('recipe save')

			if 'iname2':
				iname2 = form.cleaned_data.get('iname2')
			if 'quantity2':
				quantity2 = form.cleaned_data.get('quantity2')
			if 'unit2':
				unit2 = form.cleaned_data.get('unit2')
			if 'iname3':
				iname3 = form.cleaned_data.get('iname3')
			if 'quantity3':
				quantity3 = form.cleaned_data.get('quantity3')
			if 'unit3':
				unit3 = form.cleaned_data.get('unit3')
			if 'tags':
				# get the list of tag number
				tags = form.cleaned_data.get('tags')

			# get current last igid
			last_igid = Ingredient.objects.all().latest('igid')

			# save ingredient to db
			ingredient = Ingredient(igid = last_igid.igid+1, iname = iname1, quantity = quantity1, cunit = unit1, rid = recipe)
			ingredient.save()
			print('ingredient save')

			if iname2 and quantity2 and unit2:
				last_igid = Ingredient.objects.all().latest('igid')
				ingredient = Ingredient(igid = last_igid.igid+1, iname = iname2, quantity = quantity2, cunit = unit2, rid = recipe)
				ingredient.save()

			if iname3 and quantity3 and unit3:
				last_igid = Ingredient.objects.all().latest('igid')
				ingredient = Ingredient(igid = last_igid.igid+1, iname = iname3, quantity = quantity3, cunit = unit3, rid = recipe)
				ingredient.save()

			# saven tag to db
			if tags :
				if tags[0] == '1' :
					tags = 'Cake'
				elif tags[0] == 2 :
					tags = 'Bread'
				elif tags[0] == 3 :
					tags = 'Itali food'
				elif tags[0] == 4 :
					tags = 'Chinese food'
				else :
					tags = 'Korea food'

				# get current last id
				last_id = Tag.objects.all().latest('id')
				tag = Tag(id = last_id.id+1, tname = tags, rid = recipe)
				tag.save()

			return HttpResponseRedirect(reverse('recipes'))

	context = {'login': True}
	return render(request, 'recipe/new_recipe.html', context)

