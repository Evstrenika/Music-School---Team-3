from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Students(models.Model):
    student = models.OneToOneField(User)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=3000)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    facebook = models.CharField(max_length=200)
    #password

    def create_profile(sender, **kwargs):
        if kwargs['created']: 
            student = Students.objects.create(student=kwargs['instance'])

    post_save.connect(create_profile,sender=User)
    
    def __unicode__(self):
        return '/%s/' % self.first_name

    def get_absolute_url(self):
        return '/students/%s/' % self.id