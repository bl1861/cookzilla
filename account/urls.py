from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^recipes/$', views.recipes, name='recipes'),
	url(r'^groups/$', views.groups, name='groups'),
	url(r'^reviews/$', views.reviews, name='reviews'),
	url(r'^groups/(?P<id>\d+)/new_event/$', views.new_event, name='new_event'),
]

