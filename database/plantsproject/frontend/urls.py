from django.conf.urls import *

from . import views

urlpatterns= [
	url(r'^$', views.cardview, name='index'),
    url(r'^edit/$', views.editPlant, name='editPlant'),
    url(r'^edit/(?P<latinName>\w+)/(?P<commonName>\w+)/(?P<imgUrl>\w+)/$', views.editPlant, name='editPlant'),
    url(r'^edit/(?P<latinName>\w+)/(?P<commonName>\w+)/$', views.editPlant, name='editPlant'),
    url(r'^edit/(?P<latinName>\w+)/(?P<commonName>\w+)/$', views.editPlant, name='editPlant'),
]