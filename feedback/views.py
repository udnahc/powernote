from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from feedback.forms import ContactForm
from feedback.models import Feedback
from django.contrib.auth import logout


def feedback_page(request, feedback_page_template):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = request.POST['message']
            feedback = Feedback()            
            feedback.message = message
            feedback.demo = request.user
            feedback.save()
            logout(request)
            return render_to_response(feedback_page_template, locals())
        else:
            error = u'Your feedback is important to us !!'
            return render_to_response(feedback_page_template, locals())
    return render_to_response(feedback_page_template, locals())

