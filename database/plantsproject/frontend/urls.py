from django.conf.urls import *

from . import views

urlpatterns= [
	url(r'^$', views.addPlant, name='index'),
    url(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
    #url(r'^getValues/(?P<attribute>\w+)/(?P<default>([\w ]+))/$', views.getAttributeValues, name='getAttributeValues'),
    url(r'^reload_controls/(?P<className>\w+)/(?P<default>([-\w ]+))/$', views.reload_attribute_vals_view, name='reload_controls'),
    url(r'^updateText/$', views.updateText, name='updateText'),
    url(r'^updateSelect/$', views.updateSelect, name='updateSelect'),
    url(r'^updateMulti/$', views.updateMulti, name='updateMulti'),
    url(r'^updateNames/$', views.updateNames, name='updateNames'),
]