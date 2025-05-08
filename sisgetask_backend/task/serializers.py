from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'start_date', 'updated_at', 'end_date']
        extra_kwargs = {
            'status': {'required': True, 'allow_blank': False},
            'name': {'required': True, 'allow_blank': False},
            'description': {'required': False},
        }
        