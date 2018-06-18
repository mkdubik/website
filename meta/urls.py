from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    re_path('', include('brew.urls')),
    path('projects/', views.projects),
    path('en/', views.home_en),
    path('is/', views.home_is),
    path('', views.home),
]



