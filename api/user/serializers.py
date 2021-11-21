from rest_framework import serializers

from core.models import User


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'email', 'is_teacher', 'first_name', 'last_name')
        fields = read_only_fields


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'email', 'is_teacher')
        fields = read_only_fields + ('first_name', 'last_name')