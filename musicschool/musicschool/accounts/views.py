from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from accounts.forms import ApplicationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return TemplateResponse(request,'pages/home.html', {})

def application(request):
    if request.method =='POST':
        form = ApplicationForm(request.POST)
        if form.is_valid(): # handles validation
            form.save()
            return redirect('/accounts')
    else:
        form = ApplicationForm()
        args = {'form' : form}
        return TemplateResponse(request,'pages/application_form.html', args)

def profile(request):
    args = {'user': request.user}
    return TemplateResponse(request,'pages/profile.html', args)