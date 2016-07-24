"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from login.views import *
import django.contrib.auth.views

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    #url(r'^home/$', home),
    #url(r'^home/', include('frontend.urls')),
    url(r'^login/$', django.contrib.auth.views.login, name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page':'/'}, name='logout'),
    url(r'^', include('frontend.urls')),
    url(r'^composer/', include('composer.urls')),
    ]