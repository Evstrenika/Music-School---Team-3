from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from accounts.forms import ApplicationForm, TeacherForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from students.models import Students
from teachers.models import Teachers
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return TemplateResponse(request,'pages/home.html', {})

def application(request):
    if request.method =='POST':
        form = ApplicationForm(request.POST)
        if form.is_valid(): # validation logic
            form.save()
            return redirect('/accounts')
    else:
        form = ApplicationForm()
        args = {'form' : form}
        return TemplateResponse(request,'pages/application_form.html', args)

def teacher_application(request): # unimplement does nothing
    if request.method =='POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = TeacherForm()
        args = {'form' : form}
        return TemplateResponse(request,'pages/teacher_form.html', args)

def students(request):
    data = Students.objects.all()
    return TemplateResponse(request,'pages/students.html', {"data" : data})

def teachers(request):
    data = Teachers.objects.all()
    return TemplateResponse(request,'pages/teachers.html', {"data" : data})

@login_required
def profile(request):
    args = {'user': request.user}
    return TemplateResponse(request,'pages/profile.html', args)

@login_required
def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save() 
            return redirect('accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = { 'form': form }
        return TemplateResponse(request, 'pages/edit.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save() 
            update_session_auth_hash(request, form.user)
            return redirect('accounts/profile')
        else:
            return redirect('/account/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return TemplateResponse(request, 'pages/change_password.html', args)


class Teacher(TemplateView):
    template_name = "teacher_form.html"

    def get(self, request):
        form = Teacher()
        return TemplateResponse(request, self.template_name, {'form' : form})