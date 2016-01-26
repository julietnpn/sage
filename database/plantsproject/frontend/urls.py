from django.conf.urls import *

from . import views

urlpatterns= [
	url(r'^$', views.cardview, name='index'),
    url(r'^edit/$', views.editPlant, name='editPlant'),
]