# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import  send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contact.forms import ContactForm
from bitfunx import  settings
from bitfunx.settings import EMAIL_FROM

# Create your views here.
def emailView(request):

    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                subject = subject +'  From  ' + from_email
                send_mail(subject, message, EMAIL_FROM, ['liyan@xinole.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found!')
            return redirect('send_email_success')
    return render(request, 'contact/email.html', {'form': form})


def successView(request):

    return render(request, 'contact/success.html')


def comingView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                subject = subject + '  From  ' + from_email
                send_mail(subject, message, EMAIL_FROM, ['liyan@xinole.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found!')
            return render(request, 'promotions/coming-success.html')
    return render(request, 'promotions/coming-soon.html', {'form': form})