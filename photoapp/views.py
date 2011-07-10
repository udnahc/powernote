from django.http import HttpResponse
from django.shortcuts import render_to_response



def view_photo_home(request, photo_home_template):
    return render_to_response(photo_home_template, locals())


def view_photo_register(request, photo_home_register_template):
    return render_to_response(photo_home_register_template, locals())
