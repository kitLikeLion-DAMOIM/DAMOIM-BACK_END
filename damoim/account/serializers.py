from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            user_id = validated_data['user_id'],
            department = validated_data['department'],
            grade = validated_data['grade'],
            phone = validated_data['phone'],
            password = validated_data['password'],
            name = validated_data['name']
        )
        return user
    class Meta:
        model=User
        fields=['user_id','department','grade','phone','password', 'name']