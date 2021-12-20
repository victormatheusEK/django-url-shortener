from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import RegisterUserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)
