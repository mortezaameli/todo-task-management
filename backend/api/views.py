from rest_framework import generics
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
