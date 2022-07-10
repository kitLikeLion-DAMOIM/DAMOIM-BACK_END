from .models import Post
from rest_framework import serializers
from comment.serializers import CommentSerializer

class PostSeiralizer(serializers.ModelSerializer):
    post = CommentSerializer(many = True, read_only=True)
    class Meta:
        model = Post
        fields= ("id","title","body","group_id","post")

class PostListSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= ("id","title","body","group_id",) 