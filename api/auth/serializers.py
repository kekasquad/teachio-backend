from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = read_only_fields + (
            'email',
            'is_teacher',
            'first_name',
            'last_name',
            'password'
        )

    password = serializers.CharField(
        max_length=100,
        required=True,
        write_only=True
    )
    first_name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
    )
    last_name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
    )
    is_teacher = serializers.BooleanField(
        default=False
    )

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)

    def create(self, validated_data):
        try:
            return User.objects.create_user(**validated_data)
        except IntegrityError:
            raise ValidationError({'username': ['User with this username already exists']})
