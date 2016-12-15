from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import UserForm
from django.urls import reverse
from db.models import User,Conversion,Rsvp,Egroup,Event,GroupUser,Ingredient,Recipe,Related,Report,ReportPhoto,Review,ReviewPhoto,Tag, UserRecipeHistory
from .forms import UploadFileForm
from django.db import connection

def home(request):
	context = {'login': False}

	# Top recipes : query and calculate rate from db
	with connection.cursor() as cursor:
		cursor.execute('SELECT rid, round(avg(rating),1) as rate from review GROUP BY rid ORDER BY rate DESC')
		rows = cursor.fetchall()

	# list to store tuple (Recipe object,rate)
	top_recipes = []
	for row in rows :
		# tuple (Recipe object,rate)
		rid_avg_rate = (Recipe.objects.get(rid=row[0]) , row[1])
		top_recipes.append(rid_avg_rate)

	context['top_recipe'] = top_recipes

	if 'username' in request.session:
		context['login'] = True
		context['username'] = request.session['username']

		# history recipes : query and count recipe review times from db
		historySet = UserRecipeHistory.objects.filter(uname__uname = context['username']).order_by('-visit_time')

		# list to store tuple (Recipe object,rate)
		most_review_recipes = []
		for row in historySet :
			# tuple (Recipe object,UserRecipeHistory object)
			recipe_history = (Recipe.objects.get(rid = row.rid.rid) , row)
			most_review_recipes.append(recipe_history)

		context['most_review_recipes'] = most_review_recipes

		return render(request, 'main/home.html', context);

	return render(request, 'main/home.html',context)


def login(request):

	# if this is a POST request, we need to process the form data.
	if request.method == "POST":

		# create a form instancee and populate it with data from the request.
		form = UserForm(request.POST)

		# if the form is valid, then do something
		if form.is_valid():

			user = form.cleaned_data.get('username')
			pw = form.cleaned_data.get('password')
			dbuser = User.objects.filter(uname = user,password=pw)

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


def signup(request):

	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		print(form.is_valid())

		if form.is_valid():

			name = form.cleaned_data.get('signup_username')
			pwd = form.cleaned_data.get('signup_password')
			nickname = form.cleaned_data.get('signup_nickname')
			description = form.cleaned_data.get('signup_desc')
			file = form.cleaned_data['signup_file']
			photo = form.cleaned_data['signup_photo']

			# query from db
			cursor = connection.cursor()
			result = cursor.execute("SELECT uname from _user as u WHERE u.uname='"+name+"'")

			if result:
				return HttpResponseRedirect(reverse("signup"))

			# construct a new register user
			new_user = User(uname=name,login_name=nickname,password=pwd,udescription=description,ufile=file,uphoto=photo)
			#save to database
			new_user.save()
			return HttpResponseRedirect(reverse("login"))

	return render(request, 'main/signup.html')

def header(request):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
		context['username'] = request.session['username']
		return render(request, 'main/home.html', context);

	'''cursor = connection.cursor()
	cursor.execute('SELECT distinct tname from tag')
	tags = cursor.fetchall()

	# dictionary to store key:tag / value: recipe model list
	tag_dictionary = {}
	# list to store recipe of same tag

	for tag in tags :
		recipe_list = []
		recipe_set = Recipe.objects.raw("SELECT * from recipe inner join tag on recipe.rid=tag.rid WHERE tag.tname='"+str(tag[0])+"'")
		print(tag[0])
		for recipe in recipe_set:
			recipe_list.append(recipe)

		tag_dictionary[tag[0]] = recipe_list

	context['all_tag'] = tag_dictionary'''

	return render(request, 'main/home.html')



