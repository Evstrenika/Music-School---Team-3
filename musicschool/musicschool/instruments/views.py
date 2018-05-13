from django.shortcuts import render
from django.template.response import TemplateResponse
from instruments.models import Instruments

# Create your views here.
def instruments(request):
    data = Instruments.objects.all()
    return TemplateResponse(request,'pages/instruments.html', {"data" : data}) # curly braces dictionary list


'''
####
# 
# whatever is passed above runs server side (not static)
#
#
##
    #data = Instruments.objects.filter(name="jazz flute") # still returns a set
    #data = Instruments.objects.get(name="jazz flute") # return single object
    #data = Instruments.objects.get(pk=1) # return by primary key

'''