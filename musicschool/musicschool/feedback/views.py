from django.shortcuts import render
from django.template.response import TemplateResponse
from feedback.models import Feedback

# Create your views here.
def feedback(request):
    data = Feedback.objects.all()
    return TemplateResponse(request,'pages/feedback.html', {"data" : data})
