from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	#url(r'^$', views.profile, name='profile'),
]