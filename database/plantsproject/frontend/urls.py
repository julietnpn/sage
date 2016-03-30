from django.conf.urls import *

from . import views

urlpatterns= [
	url(r'^$', views.viewPlants, name='index'),
	url(r'^addPlant/$', views.addPlant, name='index'),
    url(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
    url(r'^search/$', views.search, name='editPlant'),
    url(r'^reload_controls/(?P<className>\w+)/(?P<default>([-\w ]+))/$', views.reload_attribute_vals_view, name='reload_controls'),
    url(r'^updateText/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateText, name='updateText'),
    url(r'^updateSelect/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateSelect, name='updateSelect'),
    url(r'^updateMulti/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateMulti, name='updateMulti'),
    url(r'^updateNames/$', views.updateNames, name='updateNames'),
    url(r'^addImg/$', views.addImg, name='updateNames'),
]