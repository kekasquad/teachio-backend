from rest_framework.generics import DestroyAPIView, CreateAPIView

from message.models import Message
from . import serializers


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageCreateSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageDestroyAPIView(DestroyAPIView):
    queryset = Message.objects.all()
    serializers = serializers.MessageRetrieveSerializer


