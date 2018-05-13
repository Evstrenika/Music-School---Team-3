from django.contrib import admin
from .models import Contracts

class ContractsAdmin(admin.ModelAdmin):
    list_display = ('lesson_type',)

admin.site.register(Contracts, ContractsAdmin)