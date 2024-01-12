from django.db import models
from django.utils import timezone

class AboutME(models.Model):
    topic=models.CharField(max_length= 30) 
    aboutme=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

def __str__(self):
    return '<Topic:{},ID:{}>'.format(self.topic,self.id)    