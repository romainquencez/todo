from django.urls import (path, include)
from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token, verify_jwt_token)

from tasks.urls import tasks_urlspatterns
from users.urls import users_urlpatterns

urlpatterns = [
    # DRF api auth
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    # JWT AUTH
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    # apps
    path('tasks/', include(tasks_urlspatterns)),
    path('users/', include(users_urlpatterns)),
]
