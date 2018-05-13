from django.contrib import admin
from .models import Parents

class ParentsAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

admin.site.register(Parents, ParentsAdmin)