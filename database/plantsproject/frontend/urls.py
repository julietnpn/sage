from django.conf.urls import *

from . import views
#from frontend.views import PlantList

urlpatterns= [
	url(r'^$', views.viewPlants, name='index'),
	url(r'^addPlant/$', views.addPlant, name='index'),
    url(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
    url(r'^search/(?P<searchString>[\w ]+)/$', views.search, name='editPlant'),
    url(r'^filter/$', views.filter),
    url(r'^reload_controls/(?P<className>\w+)/$', views.reload_attribute_vals_view, name='reload_controls'),
    url(r'^updateText/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateText, name='updateText'),
    url(r'^updateSelect/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateSelect, name='updateSelect'),
    url(r'^updateMulti/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateMulti, name='updateMulti'),
    url(r'^updateNames/$', views.updateNames, name='updateNames'),
    url(r'^removeAttribute/$', views.removeAttribute, name='removeAttribute'),
    url(r'^addImg/$', views.addImg, name='updateNames'),
    url(r'^getCharacteristic/$', views.getCharacteristics),
    url(r'^getProduct/$', views.getProducts),
    url(r'^getBehavior/$', views.getBehaviors),
    url(r'^getNeed/$', views.getNeeds),
    url(r'^getTolerance/$', views.getTolerances),
]