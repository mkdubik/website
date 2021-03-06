import traceback
import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.utils import IntegrityError
from django.template import loader
import django.contrib.gis.geoip2

from pdb import set_trace

from .models import Project

g = django.contrib.gis.geoip2.GeoIP2()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    ip = get_client_ip(request)
    try:
        if g.country(ip)['country_code'] == 'IS':
            return render_to_response('home_is.html')
        return render_to_response('home.html')
    except Exception as e:
        return render_to_response('home_is.html')

def home_en(request):
    return render_to_response('home.html')

def home_is(request):
    return render_to_response('home_is.html')

def four_zero_four(request):
    return render_to_response('404.html')

def projects(request):
    template = loader.get_template('projects.html')
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return HttpResponse(template.render(context, request))
