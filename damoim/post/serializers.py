from .models import Post
from django.core import serializers
from rest_framework import serializers
from comment.serializers import CommentSerializer

class PostSeiralizer(serializers.ModelSerializer):
    post = CommentSerializer(many = True, read_only=True)
    class Meta:
        model = Post
        fields= ("id","title","body","group_id","post","date")
    date= serializers.DateTimeField(input_formats=["%Y-%m-%h"])

class PostListSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= ("id","title","body","group_id",)

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=("group_id","title","body",)