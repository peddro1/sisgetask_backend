from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # lookup_field = 'id'
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]