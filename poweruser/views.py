# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers
from poweruser.forms import LoginForm
from poweruser.models import UserProfile

def view_sign_up(request, signup_page_template):
    return render_to_response( signup_page_template, locals())

def view_login_in(request, login_page_template):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = request.POST['username']
            email = request.POST['email']
            user_exists = UserProfile.objects.user_exists(email)
            if not user_exists:
                UserProfile.objects.save_user(name, email)
                from django.contrib.auth import authenticate
                user = authenticate(username=email, password = "%s%s" % (name,"123"))
                if user:
                    print "Logging user in "
                    from django.contrib.auth import login
                    login(request, user)
                    return HttpResponseRedirect("demo")
                else:
                    print "Authentication failed yy ?????"
            else:
                error= u"User already exists "
        else:
            error = u'Username and Password should not be empty'
            return errorHandle(error)
    else:
        form = LoginForm() # An unbound form                                          
    return render_to_response(login_page_template, locals())
