# coding=utf-8
# 自定义的过滤器和标签

from django import template
import time
from datetime import datetime

register = template.Library()


# {% load extra_tags %} 在引用的html界面加载
@register.filter(name='datetime')  # 过滤器名称
def datetimeFilter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    elif delta < 3600:
        return u'%s分钟前' % (delta // 60)
    elif delta < 86400:
        return u'{}小时前'.format(delta // 3600)
    elif delta < 604800:
        return u'{}天前'.format(delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'{}年{}月{}日'.format(dt.year, dt.month, dt.day)


@register.filter(name='cut')  # 过滤器在模板中使用时的name
def myCut(value, arg):  # 把传递过来的参数arg替换为'~'    html 传参时 {{value| cut:'arg'}}
    return value.replace(arg, '~')


# 自定义标签，格式化返回当前时间   模板中使用 {% current_time "%Y-%m-%d %H:%M:%S" %}
@register.tag(name='current_time')
# 解析器
def do_current_time(parse, token):  # parse解析器对象，token被解析的对象，包含标签的名字和格式化的格式
    try:
        tag_name, format_string = token.split_contents()
    except:
        raise template.TemplateSyntaxError('syntax')
    return CurrentNode(format_string[1:-1])  # 传入模板中的节点类


class CurrentNode(template.Node):
    def __init__(self, format):
        self.format_string = str(format)

    # 把当前时间格式化后返回
    def render(self, context):
        now = datetime.now()
        return now.strftime(self.format_string)
