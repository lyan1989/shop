from django import forms


class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True, label=r'your email address')
    subject = forms.CharField(required=True, label=r'Your name')
    message = forms.CharField(widget=forms.Textarea, required=True, label=r'Your message')




