from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from core.models import User
from core.models import ActivationCode
from core.utils import send_code
from . import serializers


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = False
        user.save()

        send_code(user)


class ActivateAPIView(GenericAPIView):
    serializer_class = serializers.UserActivateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(email=serializer.validated_data["email"])
            activation_code = ActivationCode.objects.get(user=user)
        except (User.DoesNotExist, ActivationCode.DoesNotExist):
            raise Http404

        if activation_code.code == serializer.validated_data["code"]:
            user.is_active = True
            user.save()
            activation_code.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            raise ValidationError({
                'code': 'Wrong code'
            })


class ResendActivationCode(GenericAPIView):
    serializer_class = serializers.ResendActivationCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(
                email=serializer.validated_data["email"]
            )
        except User.DoesNotExist:
            raise Http404

        if user.is_active:
            raise ValidationError({
                'email': 'User has been already activated'
            })

        send_code(user)
        return Response(status=status.HTTP_201_CREATED)
