from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_feedback',)

admin.site.register(Feedback, FeedbackAdmin)