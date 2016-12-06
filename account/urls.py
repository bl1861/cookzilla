from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.profile, name='profile'),
	url(r'^recipes/$', views.recipes, name='recipes'),
	url(r'^groups/$', views.groups, name='groups'),
	url(r'^events/$', views.events, name='events'),
	url(r'^RSVPs/$', views.rsvps, name='RSVPs'),
	url(r'^reviews/$', views.reviews, name='reviews'),
]