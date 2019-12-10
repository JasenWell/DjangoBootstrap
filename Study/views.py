# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.cache import cache_page
import json


# Create your views here.

def girdSystem(request):
    return render(request, template_name='Study/gird_system.html')


def login(request):
    return render(request, template_name='Study/test_login.html')
