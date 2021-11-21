from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    ListAPIView, DestroyAPIView, CreateAPIView
)
from rest_framework.permissions import IsAuthenticated

from chat.models import Chat
from . import serializers
from ..message.serializers import MessageRetrieveSerializer
from message.models import Message
from ..permissions import IsChatParticipant


class ChatCreateAPIView(CreateAPIView):
    queryset = Chat.objects.all().order_by('-updated', '-created')
    serializer_class = serializers.ChatCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        if self.request.user.id not in (
                serializer.validated_data['teacher'],
                serializer.validated_data['student']
        ):
            raise PermissionDenied({'error': 'User must be a member of the chat'})

        super().perform_create(serializer)


class ChatDestroyAPIView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatRetrieveSerializer
    permission_classes = (IsAuthenticated, IsChatParticipant)


class ChatListAPIView(ListAPIView):
    serializer_class = serializers.ChatRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Chat.objects.filter(teacher=self.request.user).order_by('-updated', '-created')
        else:
            return Chat.objects.filter(student=self.request.user).order_by('-updated', '-created')


class ChatMessagesAPIView(ListAPIView):
    serializer_class = MessageRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            return Message.objects.filter(
                Q(chat__student=self.request.user) | Q(chat__teacher=self.request.user),
                chat_id=self.kwargs['chat_id']
            ).order_by('-created')
        except ValidationError:
            raise Http404
