from django.contrib import admin
from .models import Skills

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill',)

# Register your models here.
admin.site.register(Skills, SkillsAdmin)