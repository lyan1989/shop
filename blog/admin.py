# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category, Tag
from django.urls import reverse
from django.utils.html import format_html
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=[
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    list_display_links=[]

    list_filter=['category',]
    search_fields=['title', 'category__name']

    actions_on_top=True
    actions_on_bottom=True

    save_on_top=True

    fields=(
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',

    )

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = 'post count'

    def operator(self, obj):
        return format_html(
            '<a href="{}">edit</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = 'operator'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

@admin.register(Category)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    fields = ('name', 'status', 'owner', 'is_nav')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


# Register your models here.