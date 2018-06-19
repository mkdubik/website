from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Log, LogEntry


def selected_brews(request, slug, year, month, day):
    template = loader.get_template('selected_brew.html')
    log = Log.objects.get(slug='%s/%s/%s/%s' % (slug, year, month, day))
    context = {
        'log': log,
        'entries': LogEntry.objects.filter(log_id=log.id)
    }
    return HttpResponse(template.render(context, request))



def brews(request):
    template = loader.get_template('home.html')
    logs = Log.objects.all().order_by('-yeast_addition')
    context = {
        'logs': logs
    }


    return HttpResponse(template.render(context, request))
