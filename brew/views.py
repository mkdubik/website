from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Log, LogEntry, Temperature

@csrf_exempt
def temperature(request):
    if request.method != 'POST':
        return HttpResponse(status=500)

    js = json.loads(request.body)
    print(js)
    t = Temperature(
        timestamp=js['timestamp'],
        temperature=js['temperature'],
        location=js['location'])

    t.save()

    return HttpResponse(status=200)

def selected_brews(request, slug, year, month, day):
    template = loader.get_template('selected_brew.html')
    log = Log.objects.get(slug='%s/%s/%s/%s' % (slug, year, month, day))
    context = {
        'log': log,
        'entries': LogEntry.objects.filter(log_id=log.id)
    }
    return HttpResponse(template.render(context, request))

def brews(request):
    template = loader.get_template('brew.html')
    logs = Log.objects.all().order_by('-yeast_addition')
    context = {
        'logs': logs
    }


    return HttpResponse(template.render(context, request))
