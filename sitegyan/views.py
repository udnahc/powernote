# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers


def view_home_page(request, home_page_template):
    return render_to_response(home_page_template, locals())


def view_pricing_page( request, pricing_page_template):
    return render_to_response(pricing_page_template, locals()) 
