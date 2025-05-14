from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField()
    photo = models.ImageField(upload_to='photo')
    body = models.TextField()
    time = models.TimeField()
    
    def __str__(self):
        return self.title