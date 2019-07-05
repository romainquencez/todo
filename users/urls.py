from django.urls import path

from users.views import CurrentUserRetrieveView

users_urlpatterns = [
    path('me/', CurrentUserRetrieveView.as_view(), name='me'),
]
