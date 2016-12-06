from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^(?P<id>\d+)/$', views.recipe, name='recipe'),
	url(r'^new_recipe/$', views.new_recipe, name='new_recipe'),
]