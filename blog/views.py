from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
from meta.views import log_view


def index(request):
    template = loader.get_template('index.html')
    posts = Post.objects.order_by('created')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def selected_post(request, slug):
    #template = loader.get_template('post.html')
    post = Post.objects.get(slug=slug)
    context = {
        'post': post

    }
    return render(request, 'post.html', {'post': post})
