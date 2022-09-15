#Serializers allow us to convert our data from QuerySets (the data type returned by Django's ORM) to data that can easily be converted to JSON (or XML) and returned by our API.

from rest_framework import serializers
from .models import Post #Comment #User



#Post Serializer
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('user','description', 'image_uploads', 'image_link', 'video_uploads', 'video_link')


#Comment Serializer
# class CommentSerializer(serializers.HyperlinkedModelSerializer):
#     comments= serializers.HyperlinkedRelatedField(
#     many=True, 
#     view_name='comment-detail',
#     read_only=True
#     )
# # describes what fields we need to get back
#     class Meta:
#         model= Comment
#         fields= ('__all__')
#User Serializer
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     users= serializers.HyperlinkedRelatedField(
#         many=True, 
#         view_name='user-detail', 
#         read_only=True
#     )    
# # describes what fields we need to get back
#     class Meta:
#         model= User
#         fields= ('id', 'username', 'name', 'email', 'password') 
