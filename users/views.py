from rest_framework import generics

from .models import User
from .serializers import MeSerializer


class CurrentUserRetrieveView(generics.RetrieveAPIView):
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
