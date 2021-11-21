from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import SAFE_METHODS

from chat.models import Chat
from . import serializers
from ..message.serializers import MessageRetrieveSerializer
from message.models import Message


class ChatListCreateAPIView(ListCreateAPIView):
    queryset = Chat.objects.all().order_by('-updated', '-created')

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.ChatRetrieveSerializer
        return serializers.ChatCreateSerializer


class ChatRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.ChatRetrieveSerializer
        return serializers.ChatUpdateSerializer


class ChatListAPIView(ListAPIView):
    serializer_class = serializers.ChatRetrieveSerializer

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Chat.objects.filter(teacher=self.request.user).order_by('-updated', '-created')
        else:
            return Chat.objects.filter(student=self.request.user).order_by('-updated', '-created')


class ChatMessagesAPIView(ListAPIView):
    serializer_class = MessageRetrieveSerializer

    def get_queryset(self):
        try:
            return Message.objects.filter(chat_id=self.kwargs['chat_id']).order_by('-created')
        except ValidationError:
            raise Http404
