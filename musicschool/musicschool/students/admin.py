from django.contrib import admin
from .models import Students

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name', 'address','date_of_birth','phone_number', 'email_address', 'facebook')

admin.site.register(Students, StudentsAdmin)