from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from users.views import (CurrentUserRetrieveView, CurrentUserViewSet)


router = DefaultRouter()

router.register('', CurrentUserViewSet, base_name='user')

users_urlpatterns = [
    path('me/', CurrentUserRetrieveView.as_view(), name='me'),
    path('', include(router.urls)),
]
