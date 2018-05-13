from django.shortcuts import render
from django.template.response import TemplateResponse
from preferences.models import Preferences

def preferences(request):
    data = Preferences.objects.all()
    return TemplateResponse(request,'pages/prefereces.html', {"data" : data})

