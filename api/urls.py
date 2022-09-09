from django.urls import path
from . import views

urlpatterns = [
    path('post-list/', views.PostView.as_view(), name='post_list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
]