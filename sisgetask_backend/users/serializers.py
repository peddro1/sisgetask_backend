from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'password', 'email', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }
