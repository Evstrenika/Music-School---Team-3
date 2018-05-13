from django.shortcuts import render
from django.template.response import TemplateResponse
from parents.models import Parents  

def parents(request):
    data = Parents.objects.all()
    return TemplateResponse(request,'pages/parents.html', {"data" : data})

