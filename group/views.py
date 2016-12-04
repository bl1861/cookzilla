from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def group(request, id):
	context = {'login': False}
	if 'username' in request.session:
		context['login'] = True
	return render(request, 'group/group.html', context)
