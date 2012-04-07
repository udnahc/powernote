from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from feedback.forms import ContactForm
from feedback.models import Feedback
from demosite.models import DemoUser

def feedback_page(request, feedback_page_template):

    def errorHandle(error):
        form = ContactForm()
        return render_to_response(feedback_page_template, {
                          'error' : error,
                          'form' : form,
        })

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = request.POST['message']
            feedback = Feedback()
            demo = DemoUser.objects.get(personal_email = "halesh.halesh@gmail.com")
            feedback.message = message
            feedback.demo = demo
            feedback.save()
            return HttpResponseRedirect('/logout/')
        else:
            error = u'Feedback should not be empty'
            return errorHandle(error)
    else:
        form = ContactForm()
        return render_to_response(feedback_page_template, {'form': form})

