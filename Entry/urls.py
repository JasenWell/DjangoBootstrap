# coding=utf-8

from django.conf.urls import url,include
from Entry import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^home$',views.home,name='home'),
    url(r'^login',views.login,name='login')
]