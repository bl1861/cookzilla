from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SearchForm
from .models import User, Tag, Recipe, UserTagHistory, UserKeyWordHistory, UserRecipeHistory

def search(request):
	# if this is a POST request, we need to process the form data.
	if request.method == "POST":

		# create a form instancee and populate it with data from the request.
		form = SearchForm(request.POST)

		# if the form is valid, then do something
		if form.is_valid():

			# get 'keyword' from form
			keyword = form.cleaned_data.get('keyword')

			# get 'search_type' from form
			search_type = form.cleaned_data.get('search_type')

			# create url for responding search_type
			url = reverse('search_' + search_type, kwargs={'keyword': keyword})

			# redirect http response to responding search_type
			return HttpResponseRedirect(url)

	return HttpResponseRedirect(reverse('home'))


def search_tag(request, keyword):
	context = {'login': False, 'search_type': 'tag'}
	if 'username' in request.session:
		client = request.session['username']
		context['username'] = client
		context['login'] = True

		# check if this record exist in current db or not
		print(keyword)

		tags = Tag.objects.filter(tname=keyword)
		if tags :
			record = UserTagHistory.objects.filter(uname = client, tname = tags[0])

			# if no record, save user visit tag history
			if not record:
				print(tags)
				tags = Tag.objects.filter(tname=keyword)
				user_tag_history = UserTagHistory(uname = User.objects.get(uname=client), tname = tags[0].tname)
				user_tag_history.save()
				print('save tag successfully !')


	# get the Queryset of tag for the keyword
	tag_set = Tag.objects.filter(tname=keyword)
	context['keyword'] = keyword
	context['tag_set'] = tag_set
	return render(request, 'search/search.html', context)



def search_title(request, keyword):
	context = {'login': False, 'search_type': 'title'}
	if 'username' in request.session:
		client = request.session['username']
		context['username'] = client
		context['login'] = True

		# save user search title history
		user_key_history = UserKeyWordHistory(uname = client, keyword = keyword)
		user_key_history.save()
		print('save keyword successfully !')

		# get the Queryset of recipe title
		result_title = Recipe.objects.filter(rtitle__icontains=keyword)
		arr = []
		for title in result_title:
			arr.append(title)

		context['result_title'] = arr


	return render(request, 'search/search.html', context)



def search_content(request, keyword):
	context = {'login': False, 'search_type': 'content'}
	if 'username' in request.session:
		client = request.session['username']
		context['username'] = client
		context['login'] = True

		# save user search content history
		user_key_history = UserKeyWordHistory(uname = client, keyword = keyword)
		user_key_history.save()
		print('save keyword successfully !')

		# get the Queryset of recipe content
		result_content = Recipe.objects.filter(rcontent__icontains=keyword)
		arr = []
		for content in result_content:
			arr.append(content)

		context['result_content'] = arr

	return render(request, 'search/search.html', context)
