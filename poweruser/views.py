# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.utils import simplejson
from django.core import serializers
from poweruser.forms import LoginForm
from demosite.models import DemoUser

def view_sign_up(request, signup_page_template):
    return render_to_response( signup_page_template, locals())

def view_logout(request, logout_page_template):
    return render_to_response( logout_page_template, locals())

def view_login_in(request, login_page_template):

    def errorHandle(error):
        form = LoginForm()
        return render_to_response(login_page_template, {
                          'error' : error,
                          'form' : form,
        })
    if request.method == 'POST': # If the form has been submitted...                                                                                         
        form = LoginForm(request.POST) # A form bound to the POST data                                                                                       
        if form.is_valid(): # All validation rules pass
            username = request.POST['username']
            email = request.POST['email']
            demo_user = DemoUser()
            demo_user.username = username
            demo_user.personal_email = email
            demo_user.save()
            return HttpResponseRedirect('/demo/')
        else:
            error = u'Username and Password should not be empty'
            return errorHandle(error)
    else:
        form = LoginForm() # An unbound form                                                                                                                 
        return render_to_response(login_page_template, {
                'form': form,
                })
