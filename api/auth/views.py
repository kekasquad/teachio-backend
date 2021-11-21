from rest_framework.generics import CreateAPIView
from core.models import User
from . import serializers


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserCreateSerializer
