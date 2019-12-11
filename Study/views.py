# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.cache import cache_page
from django.urls import reverse
import json

namespace = 'Sduty'
# Create your views here.

def checkLoginStatus(func):
    def func_in(request):
        print('check login',request)
        if request.session.get('username'):
            result = func(request);
            return result
        else:
            request.session['username'] = 'hjh'
            print(reverse(login))
            return HttpResponseRedirect('/test/login')
    return func_in


@checkLoginStatus
def girdSystem(request):
    return render(request, template_name='Study/gird_system.html')


def login(request):
    return render(request, template_name='Study/test_login.html')

def home(request):
    pass