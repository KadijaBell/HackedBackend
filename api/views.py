from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import UserSerializer,PostSerializer,CommentSerializer

User = get_user_model()

# Create your views here.
# Post List View


#class based view
class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class CommentView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


#Authentication View
class SignUpView(APIView):
#handles post request from view
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials, wish I could tell you which one'})

    def post(self, request):
#getting data from form
        email = request.data.get('email')
        #username=request.data.get('username')
        password = request.data.get('password')

        user = self.get_user(email)
        #user = self.get_user(username)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials, wish I could tell you which one'})
#if everything checks out then we can create a token
        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome to the hacks,  {user.username}!'})