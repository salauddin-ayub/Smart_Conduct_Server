from rest_framework import serializers
from room.models import Registration


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['firstName', 'lastName', 'phone', 'email', 'created_at']
