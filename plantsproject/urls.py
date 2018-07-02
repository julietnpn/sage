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
from django.urls import *
from django.contrib import admin
from login.views import *
import django.contrib.auth.views

# urlpatterns = [
#     path(r'^admin/', include(admin.site.urls)),
# ]


urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^register/$', register),
    re_path(r'^register/success/$', register_success),
    re_path(r'^view_profile/$', view_profile),
    #path(r'^home/$', home),
    #path(r'^home/', frontend.urls),
    re_path(r'^login/$', django.contrib.auth.views.login, name='login'),
    re_path(r'^logout/$', django.contrib.auth.views.logout, {'next_page':'/'}, name='logout'),
    re_path(r'^', include('frontend.urls')),
    re_path(r'^comments/', include('django_comments_xtd.urls')),
]


    #path(r'^composer/',composer.urls),