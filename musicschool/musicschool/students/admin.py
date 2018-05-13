from django.contrib import admin
from .models import Students

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

admin.site.register(Students, StudentsAdmin)