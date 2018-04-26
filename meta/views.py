import traceback
import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.utils import IntegrityError
import django.contrib.gis.geoip2 

from .models import Visitor

from pdb import set_trace

g = django.contrib.gis.geoip2.GeoIP2()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_view(func):
    def wrapper(*args, **kwargs):
        req = args[0]

        v = Visitor(
            ip=get_client_ip(req),
            ua=req.META.get('HTTP_USER_AGENT', '')[:99],
            referer=req.META.get('HTTP_REFERER', ''),
            path=req.get_full_path())

        try:
            v.save()
        except IntegrityError as e:
            pass

        return func(*args, **kwargs)
    return wrapper

@log_view
def home(request):
    ip = get_client_ip(request)
    try:
        if g.country(ip)['country_code'] == 'IS':
            return render_to_response('home_is.html')
        return render_to_response('home.html')
    except Exception as e:
        return render_to_response('home_is.html')

@log_view
def home_is(request):
    return render_to_response('home_is.html')

@log_view
def home_en(request):
    return render_to_response('home.html')

@log_view
def four_zero_four(request):
    return render_to_response('404.html')
