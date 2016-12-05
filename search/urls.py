from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.search, name='search'),
	url(r'^tag/(?P<keyword>\w+)/$', views.search_tag, name='search_tag'),
	url(r'^title/(?P<keyword>\w+)/$', views.search_title, name='search_title'),
	url(r'^content/(?P<keyword>\w+)/$', views.search_content, name='search_content')
]