from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RecipeForm, ReviewForm
from django.urls import reverse
from .models import User, Recipe, Egroup, Event, Rsvp, Tag, Review, Ingredient, ReviewPhoto, UserRecipeHistory, Conversion
import datetime

# Create your views here.
def recipe(request, id):

	# create dictrionary of corresponding review & ingredient for thos recipe
	recipe_dictionary = {}

	# get Recipe
	recipe = Recipe.objects.filter(rid = id)
	recipe_dictionary['recipe'] = recipe

	# get Review Queryset
	reviews = Review.objects.filter(rid__rid = id)

	# set default rating =0
	avg_rating = 0
	count = 0

	rw_dictionary = {}
	for rw in reviews:
		# calcualte average rating
		count += 1
		avg_rating = (avg_rating + rw.rating)/count
		#get the review photo
		rwpicture = ReviewPhoto.objects.filter(rwid__rwid = rw.rwid)
		if rwpicture :
			rw_dictionary[rw] = rwpicture[0]
		else:
			rw_dictionary[rw] = None

	recipe_dictionary['review'] = rw_dictionary

	#
	unit_dictionary={}	
	ingredients = Ingredient.objects.filter(rid__rid = id)

	unit_set = Conversion.objects.all()

	for ing in ingredients:
		ingredients_dictionary={}
		for unit in unit_set:
			if ing.cunit == unit.cunit:
				ingredients_dictionary[ing.cunit] = ing.quantity
			else:
				ingredients_dictionary[unit.cunit] = ing.quantity*unit.cquantity

		unit_dictionary[ing] = ingredients_dictionary


	recipe_dictionary['ingredient'] = unit_dictionary

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

	context = {'login': False}
	client = '____'

	if 'username' in request.session:
		context['login'] = True
		client= request.session['username']
		context['username'] = client

		# check if this record exist in current db or not
		record = UserRecipeHistory.objects.filter(uname = User.objects.get(uname=client), rid = recipe[0])

		# if no record, save user visit recipe history
		if not record:
			user_recipe_history = UserRecipeHistory(uname = User.objects.get(uname=client), rid = recipe[0], visit_time = datetime.datetime.now())
			user_recipe_history.save()
			print('save recipe history successfully !')

		# if this is a POST request, we need to process the form data.
		if request.method == "POST":
			form = ReviewForm(request.POST, request.FILES)
			if form.is_valid():
				print('review_post_valid')
				review_title = form.cleaned_data.get('review_title')
				review_context = form.cleaned_data.get('review_context')

				# constrct the review model
				review = Review(uname = User.objects.get(uname=client), rwtitle= review_title, rwcontext = review_context, rid = recipe[0])

				if 'review_suggestion' :
					review.suggestion = form.cleaned_data.get('review_suggestion')
				if 'review_rating' :
					review.rating = form.cleaned_data.get('review_rating')
				else :
					review.rating =0
				# save to db
				review.save()

				# if user attach file, get the file and save to db
				if 'review_photo' :
					review_photo = form.cleaned_data.get('review_photo')
					rwphoto = ReviewPhoto(rwid = review, rw_photo = review_photo)
					rwphoto.save()
					rwphoto.rw_photo_name = rwphoto.rw_photo.name
					rwphoto.save()

				return HttpResponseRedirect("/recipe/%s/" % id)

	context = {'account_item': 'Recipes' ,'login': True, 'recipe_dictionary': recipe_dictionary, 'avg_rating':avg_rating, 'tags':tags}
	context['username'] = client

	return render(request, 'recipe/recipe.html', context)


def new_recipe(request):
	# if the user is not login, redirect to login page
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse("login"))

	# get username login name
	client= request.session['username']

	# if this is a POST request, we need to process the form data.
	if request.method == "POST":

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

			# construct a new created recipe
			recipe = Recipe(rtitle = recipe_title, rcontent = recipe_content, rserving = recipe_servings, uname = User.objects.get(uname=client), rtime = datetime.datetime.now())

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
				print(tags)

			# save ingredient to db
			ingredient = Ingredient(iname = iname1, quantity = quantity1, cunit = unit1, rid = recipe)
			ingredient.save()
			print('ingredient save')

			if iname2 and quantity2 and unit2:
				#last_igid = Ingredient.objects.all().latest('igid')
				ingredient = Ingredient(iname = iname2, quantity = quantity2, cunit = unit2, rid = recipe)
				ingredient.save()

			if iname3 and quantity3 and unit3:
				#last_igid = Ingredient.objects.all().latest('igid')
				ingredient = Ingredient(iname = iname3, quantity = quantity3, cunit = unit3, rid = recipe)
				ingredient.save()

			# saven tag to db

			if tags :
				tag_list =[]
				for tag in tags :
					if tag == '1' :
						tag_list.append('Cake')
					if tag == '2' :
						tag_list.append('Bread')
					if tag == '3' :
						tag_list.append('Itali_food')
					if tag == '4' :
						tag_list.append('Chinese_food')
					if tag == '5':
						tag_list.append('Korea_food')

				for element in tag_list:
					# get current last id
					#last_id = Tag.objects.all().latest('id')
					print(element)
					tag = Tag(tname = element, rid = recipe)
					tag.save()

			return HttpResponseRedirect(reverse('recipes'))

	context = {'login': True}
	context['username'] = client
	return render(request, 'recipe/new_recipe.html', context)

