from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def my_custom_page_not_found_view(request, exception=None):
    html = "<html><body>It is found.</body></html>"
    return HttpResponse(html)

handler404 = my_custom_page_not_found_view