# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category, Tag
from django.urls import reverse
from django.utils.html import format_html
from bitfunx.custom_site import custom_site
from django.contrib.admin.models import LogEntry
from .adminform import PostAdminForm

class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器，只展示当前用户分类"""

    title = 'Category Filter'
    parameter_name = 'owner_catagory'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display=[
        'title', 'category', 'status', 'owner',
        'created_time', 'operator'
    ]
    list_display_links=[]
    exclude = ('owner',)
    list_filter=[CategoryOwnerFilter]
    search_fields=['title', 'category__name']

    actions_on_top=True
    actions_on_bottom=True

    save_on_top=True


    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = 'post count'

    def operator(self, obj):
        return format_html(
            '<a href="{}">edit</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = 'operator'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    fields = ('name', 'status', 'owner', 'is_nav')


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'owner', 'status')


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message')
# Register your models here.
