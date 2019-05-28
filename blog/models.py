# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import mistune


class Category(models.Model):
    STATUS_NORMAL =1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete'),
    )

    name = models.CharField(max_length=50, verbose_name='name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    is_nav = models.BooleanField(default=False, verbose_name='is nav or not')
    owner = models.ForeignKey(User, verbose_name='author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    class Meta:
        verbose_name = verbose_name_plural = 'category'

    def __str__(self):
        return self.name

    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)
        return {
            'navs' : nav_categories,
            'categories' : normal_categories,
        }


class Tag(models.Model):
    STATUS_NORMAL= 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete'),
    )

    name = models.CharField(max_length=50, verbose_name='name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    owner = models.ForeignKey(User, verbose_name='author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    class Meta:
        verbose_name = verbose_name_plural = 'tag'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete'),
        (STATUS_DRAFT, 'draft'),
    )

    title = models.CharField(max_length=255, verbose_name='title')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='abstract')
    content = models.TextField(verbose_name='content',help_text='markdown format needed')
    content_html = models.TextField(verbose_name="正文html代码", blank=True, editable=False)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    tag = models.ForeignKey(Tag, verbose_name='tag')
    category = models.ForeignKey(Category, verbose_name='category')
    owner = models.ForeignKey(User, verbose_name='author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created time')

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)



    class Meta:
        verbose_name = verbose_name_plural = 'article'
        ordering = ['-created_time'] #根据ID进行降序

    def save(self, *args, **kwargs):
        self.content_html = self.content
        super(Post, self).save(*args, **kwargs)

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv')

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id = category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        return post_list, category

    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.filter(status=cls.STATUS_NORMAL)


# Create your models here.
