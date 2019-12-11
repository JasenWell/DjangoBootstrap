# coding=utf-8
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.template.loader import render_to_string
import json, os

# Create your views here.
from Entry.models import Column, Article


def generateStaticPage(request):
    staticHtml = 'test.html'
    context = {'key': 'value'}
    if not os.path.exists(staticHtml):
        content = render_to_string('base.html', context)
        with open(staticHtml, 'w')as f:
            f.write(content)
    return render(request, template_name=staticHtml)


def index(request):
    columns = Column.objects.all()
    return render(request, 'Entry/index.html', {'columns': columns})


def columnDetail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'Entry/column.html', {'column': column})


def articleDetailOld(request, article_slug):
    articles = Article.objects.filter(slug=article_slug)
    for item in articles:
        print('打扫打扫打扫大所：', item.slug,item.column,item.title)
    return render(request, 'Entry/article.html', {'article': articles[0]})


def articleDetail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    print(article_slug, article.slug)
    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'Entry/article.html', {'article': article})


def home(request):
    current_namespace = request.resolver_match.namespace  # 变更部分
    print('name= ', current_namespace)
    result = reverse("%s:login" % current_namespace)
    return HttpResponse('中文home==> ' + result)
    pass


def login(request):
    return render(request, template_name='Entry/login.html')
