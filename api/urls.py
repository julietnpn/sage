from django.urls import *

from . import views


urlpatterns= [
    path('api/all-plants/', views.plant_list),
    path('api/<int:pk>/', views.plant_detail),
    path('api/', views.api_documentation),
]

