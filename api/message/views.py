from rest_framework.exceptions import ValidationError
from rest_framework.generics import DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from chat.models import Chat
from message.models import Message
from . import serializers
from ..permissions import IsMessageSender


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        try:
            chat = serializer.validated_data['chat']
            if str(self.request.user.pk) not in (str(chat.student.pk), str(chat.teacher.pk)):
                raise ValidationError({'error': 'User must be a member of the chat'})
        except Chat.DoesNotExist:
            raise ValidationError({'chat': 'Chat does not exist'})
        serializer.save(sender=self.request.user)


class MessageDestroyAPIView(DestroyAPIView):
    queryset = Message.objects.all()
    serializers = serializers.MessageRetrieveSerializer
    permission_classes = (IsAuthenticated, IsMessageSender)


