from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('post/', views.PostDetails.as_view(), name='post_detail'),
    path('post/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),



    ]