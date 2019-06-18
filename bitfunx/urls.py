"""bitfunx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from oscar.app import application
from bitfunx.custom_site import custom_site
from blog.views import post_detail, post_list, links, MyView, PostDetailView, IndexView, \
    CategoryView,TagView, SearchView, AuthorView, LinkView
from django.views.generic import TemplateView
from comment.views import CommentView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    # Optional
    #url(r'^dashboard/paypal/express/', application.urls),
    url(r'^super_admin/', include(admin.site.urls)),
    url(r'^admin/', include(custom_site.urls)),
    url(r'^contact/', include('contact.urls')),
    url(r'^category/(?P<category_id>\d+)$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(), name='post-detail'),
    url(r'^blog/$', IndexView.as_view(), name='blog'),
    url(r'^blog/about/$', TemplateView.as_view(template_name="blog/about.html")),
    url(r'^links/$', LinkView.as_view(), name='links'),
    url(r'^blog/search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'', include(application.urls)),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

