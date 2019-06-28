from rest_framework import (mixins, viewsets)
from rest_framework.permissions import IsAdminUser

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    permission_classes = (IsAdminUser, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
