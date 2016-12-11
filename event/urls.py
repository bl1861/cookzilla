from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^(?P<id>\d+)/$', views.event, name='event'),
	url(r'^(?P<id>\d+)/report/$', views.report, name='report'),
]