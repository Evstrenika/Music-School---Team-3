from django.db import models

class Instruments(models.Model):
    instrument_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    condition = models.CharField(max_length=200)
    hired = models.BooleanField(default=False)
    
    def __unicode__(self):
        return '/%s/' % self.name # i.e this

    def get_absolute_url(self):
        return '/instruments/%s/' % self.id

'''

python manage.py makemigrations
python manage.py migrate


'''

