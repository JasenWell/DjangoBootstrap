# coding=utf-8
from django.conf.urls import url, include
from Study import views

urlpatterns = [
    url(r'^gird_system$', views.girdSystem, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^login', views.login, name='login')
]
