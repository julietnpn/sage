from django.urls import *

from . import views


urlpatterns= [
    path('', views.viewPlants, name='index'),
    re_path(r'^addPlant/$', views.addPlant, name='index'),
    re_path(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
    re_path(r'^search/(?P<searchString>[\w ]+)/$', views.search, name='editPlant'),
    re_path(r'^filter/$', views.filter),
    re_path(r'^reload_controls/(?P<className>\w+)/$', views.reload_attribute_vals_view, name='reload_controls'),
    re_path(r'^updateText/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateText, name='updateText'),
    re_path(r'^updateSelect/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateSelect, name='updateSelect'),
    re_path(r'^updateMulti/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateMulti, name='updateMulti'),
    re_path(r'^updateNames/$', views.updateNames, name='updateNames'),
    re_path(r'^removeAttribute/$', views.removeAttribute, name='removeAttribute'),
    re_path(r'^addImg/$', views.addImg, name='updateNames'),
    re_path(r'getCharacteristic/$', views.getCharacteristics),
    re_path(r'^getProduct/$', views.getProducts),
    re_path(r'^getBehavior/$', views.getBehaviors),
    re_path(r'^getNeed/$', views.getNeeds),
    re_path(r'^getTolerance/$', views.getTolerances),
    path('about/', views.about),
    re_path(r'^view_contributor/([0-9]+)/$', views.view_contributor),
]



# urlpatterns= [
#     path('', views.viewPlants, name='index'),
#     path('addPlant/', views.addPlant, name='index'),
#     re_path(r'edit/([0-9]+)/$', views.editPlant, name='editPlant'),
#     path('search/(<searchString>[\w ]+)/', views.search, name='editPlant'),
#     path('filter/', views.filter),
#     path('reload_controls/(<className>\w+)/', views.reload_attribute_vals_view, name='reload_controls'),
#     path('updateText/(<int:transaction_id>)/(<action_type>\w+)/', views.updateText, name='updateText'),
#     path('updateSelect/(<int:transaction_id>)/(<action_type>\w+)/', views.updateSelect, name='updateSelect'),
#     path('updateMulti/(<int:transaction_id>)/(<action_type>\w+)/', views.updateMulti, name='updateMulti'),
#     path('updateNames/', views.updateNames, name='updateNames'),
#     path('removeAttribute/', views.removeAttribute, name='removeAttribute'),
#     path('addImg/', views.addImg, name='updateNames'),
#     path('getCharacteristic/', views.getCharacteristics),
#     path('getProduct/', views.getProducts),
#     path('getBehavior/', views.getBehaviors),
#     path('getNeed/', views.getNeeds),
#     path('getTolerance/', views.getTolerances),
#     path('about/', views.about),
# ]


# from django.conf.urls import *
# 
# from . import views
# #from frontend.views import PlantList
# 
# urlpatterns= [
#   url(r'^$', views.viewPlants, name='index'),
#   url(r'^addPlant/$', views.addPlant, name='index'),
#   url(r'^edit/([0-9]+)/$', views.editPlant, name='editPlant'),
#   url(r'^search/(?P<searchString>[\w ]+)/$', views.search, name='editPlant'),
#   url(r'^filter/$', views.filter),
#   url(r'^reload_controls/(?P<className>\w+)/$', views.reload_attribute_vals_view, name='reload_controls'),
#   url(r'^updateText/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateText, name='updateText'),
#   url(r'^updateSelect/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateSelect, name='updateSelect'),
#   url(r'^updateMulti/(?P<transaction_id>[0-9]+)/(?P<action_type>\w+)/$', views.updateMulti, name='updateMulti'),
#   url(r'^updateNames/$', views.updateNames, name='updateNames'),
#   url(r'^removeAttribute/$', views.removeAttribute, name='removeAttribute'),
#   url(r'^addImg/$', views.addImg, name='updateNames'),
#   url(r'^getCharacteristic/$', views.getCharacteristics),
#   url(r'^getProduct/$', views.getProducts),
#   url(r'^getBehavior/$', views.getBehaviors),
#   url(r'^getNeed/$', views.getNeeds),
#   url(r'^getTolerance/$', views.getTolerances),
#   url(r'^about/$', views.about),
# ]