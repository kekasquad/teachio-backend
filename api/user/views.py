from django.contrib.auth.models import AnonymousUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from core.models import User
from . import serializers


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.UserRetrieveSerializer
        return serializers.UserUpdateSerializer


class CurrentUserAPIView(RetrieveAPIView):
    serializer_class = serializers.UserRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        if isinstance(user,  AnonymousUser):
            return Response({'error': 'No token'}, content_type='application/json', status=401)
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data)
