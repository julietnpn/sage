"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  path(r'^blog/', include(blog_urls))
"""
from django.urls import include, path
from django.contrib import admin
from login.views import *
import django.contrib.auth.views

# urlpatterns = [
#     path(r'^admin/', include(admin.site.urls)),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('register/success/', register_success),
    path('login/', django.contrib.auth.views.login, name='login'),
    path('logout/', django.contrib.auth.views.logout, {'next_page':'/'}, name='logout'),
    path('', include('frontend.urls')),
]


    #path(r'^composer/',composer.urls),