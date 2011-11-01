# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers


def view_sign_up(request, signup_page_template):
    return render_to_response( signup_page_template, locals())

def view_login_in(request, login_page_template):
    return render_to_response( login_page_template, locals())
