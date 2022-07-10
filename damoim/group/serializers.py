from .models import Group
from rest_framework import serializers
from post.serializers import PostSeiralizer,PostListSeiralizer
class GroupSerializer(serializers.ModelSerializer):
    group=PostListSeiralizer(many=True,read_only=True)
    
    class Meta:
        model = Group
        fields=("id","group_category","logo","group_name","profile_link","location","detail","group")

class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields='__all__'