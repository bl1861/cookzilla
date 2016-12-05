from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.group_all, name='group_all'),
	url(r'^(?P<id>\d+)/$', views.group, name='group'),
]