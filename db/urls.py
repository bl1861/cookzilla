from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.create_mydb, name='create_mydb'),
]