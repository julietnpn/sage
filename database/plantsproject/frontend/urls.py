from django.conf.urls import *

from . import views

urlpatterns= [
	url(r'^$', views.addPlant, name='index'),
    url(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
    url(r'^getValues/(?P<attribute>\w+)/(?P<default>([\w ]+))/$', views.getAttributeValues, name='getAttributeValues'),
    #url(r'^search/(?P<searchString>([\w ]+))/$', views.addPlant, name='search'),
    #url(r'^update/$', views.update, name='update'),
    #url(r'^getForm/(?P<className>\w+)/(?P<fieldType>\w+)/$', views.getFormForProperty, name='getForm'),
    url(r'^reload_controls/(?P<className>\w+)/(?P<default>([\w ]+))/$', views.reload_attribute_vals_view, name='reload_controls'),
]