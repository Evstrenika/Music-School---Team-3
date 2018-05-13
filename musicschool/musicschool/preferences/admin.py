from django.contrib import admin
from .models import Preferences

class PreferencesAdmin(admin.ModelAdmin):
    list_display = ('student_id',)

admin.site.register(Preferences, PreferencesAdmin)