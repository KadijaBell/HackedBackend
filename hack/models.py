
from django.db import models
from django.conf import settings

# Create your models here.


# Post Model: Display the post title, author, and body
class Post(models.Model):
    username = models.CharField(max_length=100, unique=True) 
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100)
    image_link= models.URLField(max_length=700, default='',blank=True, null=True)
    video_link= models.URLField(max_length=700, default='', blank=True, null=True)

    def __str__(self):
        return self.title
