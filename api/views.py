from django.contrib.auth.models import User
from rest_framework import generics

from .permissions import IsAnonCreate
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAnonCreate, )

    def get_queryset(self):
        user_id = self.request.user.id
        return User.objects.filter(id=user_id)


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAnonCreate, )

    def get_queryset(self):
        user_id = self.request.user.id
        return User.objects.filter(id=user_id)
