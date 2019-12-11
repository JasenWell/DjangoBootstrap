# coding=utf-8

from django.conf.urls import url, include
from Entry import views

#app_name = 'entry'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^login', views.login, name='login'),

    url(r'^column/(?P<column_slug>[^/]+)/$', views.columnDetail, name='column'),
    url(r'^news/(?P<article_slug>[^/]+)/$', views.articleDetailOld, name='article'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', views.articleDetail, name='article'),

    #pk 是Primary Key 主键的意思，这里等价于 id，但是 id 是 Python 中的一个内置函数，所以我更喜欢用 pk
]
