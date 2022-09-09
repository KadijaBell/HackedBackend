from django.db import models

# Create your models here.
# Post Model: Display the post title, author, and body
class Post(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_uploads = models.ImageField(upload_to='images/', blank=True
)
    image_link= models.URLField(max_length=255, default='String',blank=True)
    video_uploads = models.FileField(upload_to='videos/', blank=True)
    video_link= models.URLField(max_length=255, default='String', blank=True)

    def __str__(self):
        return self.title

# Comment: Display the comment body, author, and post
class Comment(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title