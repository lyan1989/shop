from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label= 'nickname',
        max_length = 50,
        widget=forms.widgets.Input(
            attrs={
                'class' : 'form-control',
                'style' : "width:60%;"
            }
        )
    )
    email = forms.CharField(
        label= 'Email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={
                'class': 'form-control',
                'style': "width:60%;"
            }
        )
    )
    website = forms.CharField(
        label='website',
        max_length= 200,
        widget=forms.widgets.URLInput(
            attrs={
                'class': 'form-control',
                'style': "width:60%;"
            }
        )
    )
    content = forms.CharField(
        label= 'Content',
        max_length= 2000,
        widget=forms.widgets.Input(
            attrs={
                'class': 'form-control',
                'style': "width:60%;"
            }
        )

    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('Comment content indicates more than 10 characters')
        return content


    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content' ]


