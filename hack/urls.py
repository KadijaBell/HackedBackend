from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
   path('posts/', views.PostList.as_view(), name='post_list'),
   path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),



    ]