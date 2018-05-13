from django.shortcuts import render
from django.template.response import TemplateResponse
from teachers.models import Teachers

def teachers(request):
    data = Teachers.objects.all()
    return TemplateResponse(request,'pages/teachers.html', {"data" : data})

