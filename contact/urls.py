from django.conf.urls import include, url
from . import views
urlpatterns = [

    url(r'^success/', views.successView, name='send_email_success'),
    url(r'^email/', views.emailView, name='email'),
    url(r'^$', views.emailView, name='contact_us'),

]
