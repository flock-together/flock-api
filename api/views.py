from django.contrib.auth.models import User
from rest_framework import generics

from .models import Event
from .permissions import IsAnonCreate, IsOwnerOrReadOnly
from .serializers import UserSerializer, EventSerializer


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


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOwnerOrReadOnly, )
