# coding=utf-8
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.cache import cache_page
from django.template.loader import render_to_string
import json,os


# Create your views here.

def generateStaticPage(request):
    staticHtml = 'test.html'
    context = {'key':'value'}
    if not os.path.exists(staticHtml):
        content = render_to_string('base.html',context)
        with open(staticHtml,'w')as f:
            f.write(content)
    return render(request,template_name=staticHtml)

def index(request):
    return HttpResponse('中文hello')




def home(request):
    pass


def login(request):
    return render(request,template_name='Entry/login.html')
