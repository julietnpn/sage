from django.urls import *

from . import views
#from frontend.views import PlantList

urlpatterns= [
    path('', views.viewPlants, name='index'),
    path('addPlant/', views.addPlant, name='index'),
    path('edit/([0-9]+)/', views.editPlant, name='editPlant'),
    path('search/(?P<searchString>[\w ]+)/', views.search, name='editPlant'),
    path('filter/', views.filter),
    path('reload_controls/(?P<className>\w+)/', views.reload_attribute_vals_view, name='reload_controls'),
    path('updateText/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/', views.updateText, name='updateText'),
    path('updateSelect/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/', views.updateSelect, name='updateSelect'),
    path('updateMulti/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/', views.updateMulti, name='updateMulti'),
    path('updateNames/', views.updateNames, name='updateNames'),
    path('removeAttribute/', views.removeAttribute, name='removeAttribute'),
    path('addImg/', views.addImg, name='updateNames'),
    path('getCharacteristic/', views.getCharacteristics),
    path('getProduct/', views.getProducts),
    path('getBehavior/', views.getBehaviors),
    path('getNeed/', views.getNeeds),
    path('getTolerance/', views.getTolerances),
    path('about/', views.about),
]