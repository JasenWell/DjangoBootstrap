# coding=utf-8
from django.db import models

# Create your models here.
from django.urls import reverse


class Column(models.Model):
    name = models.CharField(verbose_name='栏目名称', max_length=256)
    slug = models.CharField(verbose_name='栏目网址', max_length=256, db_index=True)  # db_index加速查找
    intro = models.CharField(verbose_name='栏目简介', max_length=1024, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('entry:column', args=(self.slug,))  # 指明了哪个app下的方法别名

    class Meta:
        verbose_name = '栏目'  # 模型可读名字
        verbose_name_plural = '栏目'  # 模型复数
        ordering = ['name']  # 排序字段
        # proxy = True # 表示model是其父的代理 model
        # permissions = (('can_add', 'can_add'))  # 权限控制
        # abstract = True  # 如果abstract = True 这个model就是一个抽象类


class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256,
                            db_index=True)  # unique = True, 不允许有同样值的记录存在，同时也删除了 db_index=True, 因为当 unique=True的时候会自动创索引。

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者', on_delete=True)
    content = models.TextField('内容', default='', blank=True)

    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        result = reverse('entry:article', args=(self.pk, self.slug))
        return result

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
