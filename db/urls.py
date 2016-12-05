from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.update, name='update'),
]