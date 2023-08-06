# authentication/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'age', 'department', 'section', 'batch', 'studentID', 'password', 'confirmPassword')

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirmPassword')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
