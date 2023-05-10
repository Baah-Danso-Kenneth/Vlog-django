from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    path("admin/", admin.site.urls),
    path('vlog/',include('vlog.urls',namespace='vlog_app'))
]
