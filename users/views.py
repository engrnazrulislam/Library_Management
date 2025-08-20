from django.shortcuts import render
from rest_framework import viewsets
from django.conf import settings
from .serializers import UserSerializer
User = settings.AUTH_USER_MODEL
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer