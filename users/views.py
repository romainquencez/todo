from rest_framework import (generics, mixins, viewsets)
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import MeSerializer


class CurrentUserRetrieveView(generics.RetrieveAPIView):
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user


class CurrentUserViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    serializer_class = MeSerializer
    permission_classes = (AllowAny, )

    def get_object(self):
        return self.request.user
