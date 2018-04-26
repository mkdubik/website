from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.selected_post, name='selected_post'),
]
