from django.db import models

class Preferences(models.Model):
    student_id = models.CharField(max_length=50)
    day = models.DateTimeField()
    time = models.TimeField()
    gender = models.CharField(max_length=10)
    teacher_id = models.CharField(max_length=50)

    def __unicode__(self):
        return '/%s/' % self.teacher_id

    def get_absolute_url(self):
        return '/preferences/%s/' % self.id
