from django.db import models

class Teachers(models.Model):
    teacher_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    qualifications = models.TextField(max_length=3000)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    facebook = models.CharField(max_length=200)
    #password

    def __unicode__(self):
        return '/%s/' % self.first_name

    def get_absolute_url(self):
        return '/teachers/%s/' % self.id
