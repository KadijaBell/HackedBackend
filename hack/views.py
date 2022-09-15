from rest_framework import generics
from .models import Post #Comment
from .serializers import PostSerializer #CommentSerializer



# Create your views here.


# Post Create View
class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Post List View
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Post Detail View
class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#Post update view
class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#Post Delete View
class PostDelete(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#Post Edit View
class PostEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# #Comment Create View
# class CommentCreate(generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# # Comment List View
# class CommentList(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# # Comment Detail View
# class CommentDetail(generics.RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# #Comment update/delete view
# class CommentUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

