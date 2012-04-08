from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers


def browse_photos(request, browse_photo_page_template):
    return render_to_response( browse_photo_page_template, locals())

def upload_photos(request, upload_photo_page_template):
    return render_to_response( upload_photo_page_template, locals())
