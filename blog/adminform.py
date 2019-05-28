from django import forms

from .models import Category, Tag, Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='abstract', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='content', required=False)
    class Meta:
        model = Post
        fields = (
            'category', 'tag', 'desc', 'title',  'content', 'status'
        )



