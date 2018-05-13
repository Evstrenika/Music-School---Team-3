from django.db import models

# Create your models here.
class Feedback(models.Model):
    teacher_id = models.CharField(max_length=50)
    student_feedback = models.TextField(max_length=3000)
    references_feedback = models.TextField(max_length=3000)
    
    def __unicode__(self):
        return '/%s/' % self.references_feedback

    def get_absolute_url(self):
        return '/feedback/%s/' % self.id

