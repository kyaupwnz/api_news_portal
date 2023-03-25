from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from good_news.models import NewsPost, Comments
from good_news.serializers import NewsPostSerializer, CommentsSerializer


# Create your views here.
class NewsPostViewSet(viewsets.ModelViewSet):
    serializer_class = NewsPostSerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        if self.action == 'retrieve':
            permission_classes = [AllowAny]
        if self.action == 'list':
            permission_classes = [AllowAny]
        if self.action == 'update':
            permission_classes = [IsAdminUser | IsAuthenticated]
        if self.action == 'partial_update':
            permission_classes = [IsAdminUser | IsAuthenticated]
        if self.action == 'destroy':
            permission_classes = [IsAdminUser | IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_staff:
            return NewsPost.objects.all()
        return NewsPost.objects.filter(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        if self.action == 'retrieve':
            permission_classes = [AllowAny]
        if self.action == 'list':
            permission_classes = [AllowAny]
        if self.action == 'update':
            permission_classes = [IsAdminUser | IsAuthenticated]
        if self.action == 'partial_update':
            permission_classes = [IsAdminUser | IsAuthenticated]
        if self.action == 'destroy':
            permission_classes = [IsAdminUser | IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Comments.objects.all()
        return Comments.objects.filter(author=self.request.user)
