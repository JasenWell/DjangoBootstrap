# coding=utf-8
from django.conf.urls import url, include
from Study import views

urlpatterns = [
    url(r'^$', views.test1, name='index'),
    url(r'^home$', views.test1, name='home'),
    url(r'^login', views.login, name='login')
]
