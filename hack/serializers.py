#Serializers allow us to convert our data from QuerySets (the data type returned by Django's ORM) to data that can easily be converted to JSON (or XML) and returned by our API.

from rest_framework import serializers
from .models import Post 



#Post Serializer
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('username', 'title', 'description', 'image_link', 'video_link')


