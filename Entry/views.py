# coding=utf-8
from functools import wraps

from django.http.request import RAISE_ERROR
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


def column(request):
    columns = Column.objects.all()
    return render(request, 'Entry/index.html', {'columns': columns})


def columnDetail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'Entry/column.html', {'column': column})


def articleDetailOld(request, article_slug):
    articles = Article.objects.filter(slug=article_slug)
    for item in articles:
        print('打扫打扫打扫大所：', item.slug, item.column, item.title)
    return render(request, 'Entry/article.html', {'article': articles[0]})


def articleDetail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    print(article_slug, article.slug)
    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'Entry/article.html', {'article': article})


def test(request):
    current_namespace = request.resolver_match.namespace  # 变更部分
    print('name= ', current_namespace)
    result = reverse("%s:login" % current_namespace)
    return HttpResponse('中文home==> ' + result)
    pass


# 装饰器函数，用来判断是否登录
def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.get_signed_cookie("is_login", default="0", salt="ban")
        if ret == "1":
            # 已经登录，继续执行
            return func(request, *args, **kwargs)
        # 没有登录过
        else:
            # ** 即使登录成功也只能跳转到home页面，现在通过在URL中加上next指定跳转的页面
            # 获取当前访问的URL
            next_url = request.path_info
            return redirect("/login/?next={}".format(next_url))

    return inner


@check_login
def index(request):
    return render(request, "Entry/home.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("account")
        pwd = request.POST.get("password")
        next_url = request.GET.get("next")

        if username == "hjh" and pwd == "123456":
            # return redirect("/home/")
            # 服务器返回的响应对象

            # 通过URL中的next参数指定跳转的页面，如果为空，默认跳转到home页面
            if next_url:
                print("next_url:", next_url)
                rep = redirect(next_url)
            else:
                print("ban")
                rep = redirect(reverse('Entry:home'))
            # 1. 设置cookie
            # rep.set_cookie("is_login", "1")

            # 2. 设置加盐cookie,max_age是cookie的生存时间
            rep.set_signed_cookie("is_login", "1", salt="ban",
                                  max_age=60 * 60 * 24)  # max_age单位为秒 expires和max_age默认None 在内存中，关闭浏览器则清除
            return rep
        else:
            result = {"status": 0, "data": 0, "msg": "账号或密码错误!"}
            response = HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
            return response
    else:
        return render(request, template_name='Entry/login.html')


def homeTest(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        print(account, password)
        request.session['token'] = 'hhh'
        map = {}
        map['account'] = account
        map['password'] = password

        result = {"status": 1, "data": map, "msg": "登录返回数据"}
        response = HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")
        response.set_cookie('account', account)
        response.set_cookie('password', password)  # 不加密cookie
        response.set_signed_cookie('', '', salt='encode-name')  # 加密cookie
        return response
    else:
        token = request.session.get('token', None)
        account = request.COOKIES.get('account', None)
        pwd = request.COOKIES['password']
        # request.get_signed_cookie('', default=RAISE_ERROR, salt='', max_age=None) #获取加密的cookie
        if token:
            return render(request, template_name='Entry/home.html')
        else:
            return HttpResponseRedirect('/login')


def home(request):
    # 获取cookie并判断
    # if request.COOKIES.get("is_login", 0) == "1":
    # 获取加盐cookie并判断

    ret = request.get_signed_cookie("is_login", default="0", salt="ban")
    ret = int(ret)
    if ret == 1:
        print('switch-home', ret)
        return render(request, template_name="Entry/home.html")
    else:
        print('switch-login', ret)
        return redirect("/login")


def loginOut(request):
    try:
        del request.session['token']
    except KeyError:
        pass
    result = {"status": 1, "data": '1', "msg": "登录返回数据"}
    response = HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")

    # 删除cookie,操作的是响应对象，最后需要返回
    rep = redirect("/login")
    rep.delete_cookie("is_login")
    return rep
