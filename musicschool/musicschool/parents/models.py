from django.db import models

class Parents(models.Model):
    student_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()

    def __unicode__(self):
        return '/%s/' % self.first_name

    def get_absolute_url(self):
        return '/students/%s/' % self.id
