from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated | IsAdminUser]
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        if self.action == 'update':
            permission_classes = [IsAdminUser | IsAuthenticated]
        if self.action == 'partial_update':
            permission_classes = [IsAdminUser | IsAuthenticated]
        if self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.get(pk=self.request.user.pk)

