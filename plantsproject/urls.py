"""myproject  Configuration

The `patterns` list routes s to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/s/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a  to patterns:  path(r'^$', views.home, name='home')
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
import api.views
from rest_framework import routers

# urlpatterns = [
#     path(r'^admin/', include(admin.site.urls)),
# ]



urlpatterns = [
    re_path(r'^', include('frontend.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^register/$', register),
    re_path(r'^register/success/$', register_success),
    re_path(r'^view_profile/$', view_profile),
    re_path(r'^edit_profile/$', edit_profile),
    re_path(r'^change_password/$', change_password),
    re_path(r'^view_contributor/([0-9]+)/$', view_contributor),
    #path(r'^home/$', home),
    #path(r'^home/', frontend.urls),
    #re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^login/$', django.contrib.auth.views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', django.contrib.auth.views.LogoutView.as_view(), name='logout'),
    re_path(r'^password_reset/$', django.contrib.auth.views.PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password_reset/$', django.contrib.auth.views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', django.contrib.auth.views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/$', django.contrib.auth.views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^', include('api.urls')),
    re_path(r'^comments/', include('django_comments_xtd.urls')),
    #path('django-rq/', include('django_rq.urls')),
]


    #path(r'^composer/',composer.urls),