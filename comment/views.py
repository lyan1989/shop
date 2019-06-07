# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from blog.models import Post

class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'
    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(request.POST)

        post_id = request.POST.get('target_id')
        post = get_object_or_404(Post, pk=post_id)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = post
            instance.save()
            succeed = True
        else:
            succeed = False

        context = {
            'succeed' : succeed,
            'form' : comment_form,
            'target' : post.get_absolute_url(),
        }
        return self.render_to_response(context)
# Create your views here.
