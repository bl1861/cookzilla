from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.event_all, name='event_all'),
	url(r'^(?P<id>\d+)/$', views.event, name='event'),
]