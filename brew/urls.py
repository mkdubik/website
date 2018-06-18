from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('projects/brew/', views.brews),
]



