from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet 

router = DefaultRouter()

router.register('', TaskViewSet, base_name='tasks')

tasks_urlspatterns = [
    path('', include(router.urls)),
]
