from django.conf.urls import include, url

from . import views
app_name = 'composer'
urlpatterns = [


    url(r'^$', views.UserInsert, name='UserInsert'),
    url(r'^next/$', views.Return, name='Next'),
    url(r'^address/$', views.EnterAddress, name='EnterAddress'),
    url(r'^plants/$', views.FindProducts, name='FindProducts'),
    url(r'^support/$', views.FindSupport, name='FindSupport'),
    url(r'^maps/$', views.PlantPlacement, name='PlantPlacement'),#must change here
    url(r'^id/$', views.EnterID, name='EnterID')
]