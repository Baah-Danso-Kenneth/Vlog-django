from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
from vlog.sitemaps import PostSitemap

sitemaps={
    'posts':PostSitemap,
}

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    path("admin/", admin.site.urls),
    path('vlog/',include('vlog.urls',namespace='vlog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
