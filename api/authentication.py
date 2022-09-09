from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model #User Class
from django.conf import settings # for the secret key
import jwt

User = get_user_model()

#Extends basic so you can custimize it

class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):
        header = request.headers.get('Authorization')
        if not header:
            return None
        if not header.startswith('Bearer'):
           raise PermissionDenied({'message': 'Invalid Authorization Header'})
           #if no issues grab token.  
        token = header.replace('Bearer ', '')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail='Invalid token')
        except User.DoesNotExist:
            raise PermissionDenied(detail='User not found')
        #if no issues     
        return (user, token)
