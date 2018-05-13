from django.db import models

class Contracts(models.Model):
    teacher_id = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    lesson_type = models.CharField(max_length=200)
    lesson_duration = models.DurationField()
    lesson_cost = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __unicode__(self):
        return '/%s/' % self.lesson_type

    def get_absolute_url(self):
        return '/contracts/%s/' % self.id