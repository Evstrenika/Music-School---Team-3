from django.shortcuts import render
from django.template.response import TemplateResponse
from contracts.models import Contracts

def contracts(request):
    data = Contracts.objects.all()
    return TemplateResponse(request,'pages/contracts.html', {"data" : data})
