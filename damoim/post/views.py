from .models import Post
from .serializers import PostSeiralizer
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializer_class=PostSeiralizer