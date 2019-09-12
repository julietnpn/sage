from django.urls import *

from . import views


urlpatterns= [
    re_path(r'^api/$', views.plant_list),
    path('api/<int:pk>/', views.plant_detail),
]

