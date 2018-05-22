from django.contrib import admin
from .models import Teachers

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','date_of_birth','qualifications', 'phone_number', 'email_address', 'facebook')

# Register your models here.
admin.site.register(Teachers, TeachersAdmin)