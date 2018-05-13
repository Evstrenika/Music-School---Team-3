from django.contrib import admin
from .models import Teachers

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

# Register your models here.
admin.site.register(Teachers, TeachersAdmin)