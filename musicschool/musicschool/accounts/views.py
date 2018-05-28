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
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


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
    template_name = "pages/teacher_form.html"

    def get(self, request):
        form = TeacherForm()
        return render(request, self.template_name, {'form' : form})
    
    def post(self,request):
        form = TeacherForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        qualifications = request.POST.get('qualifications')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        facebook = request.POST.get('facebook')
        
        subject = 'New Teacher Applied'
        message = (
            'Teacher Application....' + first_name + '\n' + 
            last_name + '\n' + email_address + '\n' +
            phone_number +'\n' + qualifications)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'testdevelopmentuser1@gmail.com' ] 
        send_mail(subject, message, from_email, to_email, fail_silently=False)        

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            qualifications = form.cleaned_data['qualifications']
            email_address = form.cleaned_data['email_address']
            phone_number = form.cleaned_data['phone_number']
            facebook = form.cleaned_data['facebook']

        args = {'form' : form, 'first_name' : first_name, 'last_name' : last_name,
               'date_of_birth' : date_of_birth, 'qualifications' : qualifications,
                'email_address' : email_address, 'phone_number' : phone_number,
                'facebook' : facebook }
        return TemplateResponse(request, self.template_name, args)

    

    
