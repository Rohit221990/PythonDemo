from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .forms import contactForm

def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)


def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)

def contact(request):
    title = 'Contact'
    confirm_message = 'send mail is successfull'
    form = contactForm(request.POST or None)
    if form.is_valid():
        name =  form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE'
        message = '%s %s' %(comment,name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently = True)
    context = {'title':title,'confirm_message': confirm_message,}
    template = 'contact.html'
    return render(request, template, context)

def logIn(request):
    context = locals()
    template = 'login.html'
    return render(request, template, context)

def signup(request):
    context = locals()
    template = 'signup.html'
    return render(request, template, context)
