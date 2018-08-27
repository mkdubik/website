from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'temperature', views.temperature),
    url(r'^(?P<slug>[-\w]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.selected_brews),
    url(r'', views.brews)
]
