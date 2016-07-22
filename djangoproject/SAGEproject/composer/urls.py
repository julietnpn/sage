from django.conf.urls import include, url

from . import views
app_name = 'composer'
urlpatterns = [


    url(r'^$', views.UserInsert, name='UserInsert'),
    url(r'^next/$', views.Return, name='Return'),
    url(r'^address/$', views.EnterAddress, name='EnterAddress'),
    url(r'^plants/$', views.FindProducts, name='FindProducts')
]