# from rest_framework import generics, permissions
from .models import Post 
from .serializers import PostSerializer 
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# # from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

# #Create your views here.
# Post List
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/',
        'Create': '/post_create',
        'Update': '/post_update/pk',
        'Delete': '/post/pk/delete',
        
        }

    return Response(api_urls)


# Post Create View
@api_view(['POST'])
def post_create(request):
    post = PostSerializer(data=request.data)

    if post.is_valid():
        post.save()
        return Response(post.data)
    else: 
        return Response(status=status.Http_400_BAD_REQUEST)

# Post List View
@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    post = PostSerializer(posts, many=True)
    return Response(post.data)

# Post Update View
@api_view(['POST'])
def post_update(request, pk):
    posts = Post.objects.get(pk=pk)
    post = PostSerializer(instance=post, data=request.data)

    if post.is_valid():
        post.save()
    return Response(post.data)

# Post Delete View
@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return Response('Item successfully deleted!')

# #Post Create View(POST)
# class PostCreate(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# #Post List View(GET)
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# #Post Detail View
# class PostDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    




# #Post update view(GET, PUT, PATCH and DELETE)
# # class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer
# #     permission_classes = [permissions.IsAuthenticated]
    


# # #Post Delete View(GET)
# # class PostDelete(generics.RetrieveDestroyAPIView):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# # #Post Edit View
# # class PostEdit(generics.UpdateAPIView):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer
# #     permission_classes = [permissions.IsAuthenticated]


# # #List View 
# # def posts_list(request):
# #     posts = Post.objects.all()
# #     return render(request,'posts/',{'posts' : posts} )

# # #Detail View
# # def post_detail(request, pk):
# #     post = Post.objects.get(pk=pk)
# #     return render(request, 'post/<int:pk>/edit/', {'post': post})

# # #Create View
# # def post_create(request):
# #     if request.method == 'POST':
# #         form = PostForm(request.POST)
# #         if form.is_valid():
# #             post = form.save(commit=False)
# #             post.author = request.user
# #             post.save()
# #             return redirect('posts/', pk=post.pk)
# #     else:
# #         form = PostForm()
# #     return render(request, 'post_create/', {'form': form})

# # #Edit View
# # def post_edit(request, pk):
# #     post = Post.objects.get(pk=pk)
# #     if request.method == "POST":
# #         form = PostForm(request.POST, instance=post)
# #         if form.is_valid():
# #             post = form.save(commit=False)
# #             post.username = request.user
# #             post.save()
# #             return redirect('post_detail/', pk=post.pk) 


# # #delete view
# # def post_delete(request, pk):
# #   post= Post.objects.get(pk=pk)
# #   post.delete()
# #   return redirect('posts/')
