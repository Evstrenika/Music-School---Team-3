from django.contrib import admin
from .models import Instruments

###
# 
# show by the name not just instrument object in the admin
#
#
##
class InstrumentsAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
admin.site.register(Instruments, InstrumentsAdmin)