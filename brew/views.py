from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Log

def brews(request):
    template = loader.get_template('home.html')
    logs = Log.objects.all().order_by('-yeast_addition')
    context = {
        'logs': logs
    }


    return HttpResponse(template.render(context, request))
