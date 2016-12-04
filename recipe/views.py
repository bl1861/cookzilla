from django.shortcuts import render

# Create your views here.
def recipe(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'recipe/recipe.html', context)
