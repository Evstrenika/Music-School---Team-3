from django.db import models

class Skills(models.Model):
    teacher_id = models.CharField(max_length=50)
    skill = models.CharField(max_length=200) 
    skill_level = models.CharField(max_length=200)
    language = models.CharField(max_length=200) 
     
    def __unicode__(self):
        return '/%s/' % self.skill

    def get_absolute_url(self):
        return 'skills/%s/' % self.id
