from django.db import models
from django.conf import settings

# Create your models here.


# Post Model: Display the post title, author, and body
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    image_uploads = models.ImageField(upload_to='images/', blank=True, null=True)
    image_link= models.URLField(max_length=600, default='String',blank=True, null=True)
    video_uploads = models.FileField(upload_to='videos/', blank=True,null=True)
    video_link= models.URLField(max_length=600, default='String', blank=True, null=True)

    def __str__(self):
        return self.description
