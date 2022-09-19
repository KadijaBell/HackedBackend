from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
   
   path('', views.apiOverview, name='home'),
   path('create/', views.post_create, name='post_create'),
    path('list/', views.post_list, name='post_list'),
    path('update/', views.post_update, name='post_update'),
    path('delete/', views.post_delete, name='post_delete'),

    # path('posts/', views.PostList.as_view(), name='posts_list'),
    # path('posts/', views.PostDetails.as_view(), name='posts_detail'),
    # path('posts/<int:pk>/', views.PostUpdate.as_view(), name='posts_update'),
    # path('posts/<int:pk>/', views.PostDelete.as_view(), name='post_delete'),
    # path('posts/<int:pk>/', views.PostEdit.as_view(), name='post_edit'),
    # path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
  

 ]