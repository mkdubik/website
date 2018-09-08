from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import datetime
import json

from .models import Log, Temperature

@csrf_exempt
def temperature(request):
    if request.method != 'POST':
        return HttpResponse(status=404)

    js = json.loads(request.body)
    t = Temperature(
        timestamp=datetime.datetime.strptime(js['timestamp'], '%Y-%m-%dT%H:%M:%S%z'),
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
