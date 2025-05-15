from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField()
    
    photo1 = models.ImageField(upload_to='photo')
    photo2 = models.ImageField(upload_to='photo',default="photo")
    photo3 = models.ImageField(upload_to='photo', default="photo")
    
    body = models.TextField()
    
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title