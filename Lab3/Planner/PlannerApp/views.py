from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .serializers import UserSerializer


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
