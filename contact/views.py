from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = 'Message from Cozy'
        message = '%s %s' %(form.cleaned_data['message'], name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently = True)
        title = "Thanks"
        confirm_message = "We will get right back to you!"
        form = None
    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message
        }
    template = 'contact.html'
    return render(request, template, context)
