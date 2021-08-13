
from django.conf import settings
import jwt
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import  status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth import logout


# Create your views here.

class RegisterView(GenericAPIView):

    serializer_class = UserSerializer

    def post(self,request):
        
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username = username,password=password)
        
        if user:
            auth_token = jwt.encode({
                'username': user.username},
                settings.JWT_SECRET_KEY, algorithm='HS256')
            
            serializer = UserSerializer(user)
            
            data = {
                'user':serializer.data,
                'token': auth_token
            }
            return Response(data, status = status.HTTP_200_OK)
        return Response({'response':'invalid creadentials'},status =status.HTTP_401_UNAUTHORIZED)
            
        
class LogoutView(APIView):
    def get(self, request, format=None):        
        logout(request)
        return Response(status=status.HTTP_200_OK)





