from django.shortcuts import render
from django.template.response import TemplateResponse
from skills.models import Skills

def skills(request):
    data = Skills.objects.all()
    return TemplateResponse(request,'pages/skills.html', {"data" : data})

