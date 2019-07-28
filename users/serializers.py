from rest_framework import serializers

from .models import User


class MeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'password',
            'api_url', 'api_key')
