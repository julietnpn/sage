from django.conf.urls import include, url

from . import views
app_name = 'composer'
urlpatterns = [

    path(r'^$', views.UserInsert, name='UserInsert'),
    path(r'^next/$', views.Return, name='Next'),
    path(r'^address/$', views.EnterAddress, name='EnterAddress'),
    path(r'^plants/$', views.FindProducts, name='FindProducts'),
    path(r'^goalchart/$', views.GoalChart, name='GoalChart'),
    path(r'^timeandmoney/$', views.TimeAndMoney, name='TimeAndMoney'),
    path(r'^constraints/$', views.Constraints, name='Constraints'),
    path(r'^resources/$', views.Resources, name='Resources'),
    path(r'^support/$', views.FindSupport, name='FindSupport'),
    #path(r'^maps/$', views.PlantPlacement, name='PlantPlacement'),#must change here
    path(r'^id/$', views.EnterID, name='EnterID')
]
