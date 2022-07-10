from .models import Post
from .serializers import PostSeiralizer,PostCreateSerializer,PostListSeiralizer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializer_class=PostSeiralizer


class PostListViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializer_class=PostListSeiralizer


class PostCreateViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializer_class=PostCreateSerializer