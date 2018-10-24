from django.urls import *

from . import views


urlpatterns= [
    path('', views.viewPlants, name='index'),
    re_path(r'^addPlant/$', views.addPlant, name='index'),
    re_path(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
    re_path(r'^search/(?P<searchString>[\w ]+)/$', views.search, name='editPlant'),
    re_path(r'^search//()', views.search, name='editPlant'),
    re_path(r'^filter/$', views.filter),
    re_path(r'^reload_controls/(?P<className>\w+)/$', views.reload_attribute_vals_view, name='reload_controls'),
    re_path(r'^updateText/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateText, name='updateText'),
    re_path(r'^updateSelect/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateSelect, name='updateSelect'),
    re_path(r'^updateMulti/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateMulti, name='updateMulti'),
    re_path(r'^updateNames/$', views.updateNames, name='updateNames'),
    re_path(r'^removeAttribute/$', views.removeAttribute, name='removeAttribute'),
    re_path(r'^addImg/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.addImg, name='addImg'),
    re_path(r'getCharacteristic/$', views.getCharacteristics),
    re_path(r'^getProduct/$', views.getProducts),
    re_path(r'^getBehavior/$', views.getBehaviors),
    re_path(r'^getNeed/$', views.getNeeds),
    re_path(r'^getTolerance/$', views.getTolerances),
    re_path(r'^export_plant_data/$', views.export_plant_data),
    path('about/', views.about),
    path('dbstructure', views.dbstructure),
]

