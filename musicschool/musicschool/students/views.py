from django.shortcuts import render
from django.template.response import TemplateResponse
from students.models import Students

def students(request):
    data = Students.objects.all()
    return TemplateResponse(request,'pages/students.html', {"data" : data})

