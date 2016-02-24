from django.conf.urls import *

from . import views

urlpatterns= [
	url(r'^$', views.addPlant, name='index'),
    #url(r'^edit/$', views.editPlant, name='editPlant'),
    url(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
    url(r'^getValues/(?P<attribute>\w+)/(?P<default>([\w ]+))/$', views.getAttributeValues, name='getAttributeValues'),
    url(r'^search/(?P<searchString>([\w ]+))/$', views.addPlant, name='search'),
    #url(r'^getValues/$', views.getAttributeValues, name='getAttributeValues'),
    #url(r'^edit/(?P<latinName>\w+)/(?P<commonName>\w+)/(?P<imgUrl>\w+)/$', views.editPlant, name='editPlant'),
    #url(r'^edit/(?P<latinName>\w+)/(?P<commonName>\w+)/$', views.editPlant, name='editPlant'),
]