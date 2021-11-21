from rest_framework import serializers

from message.models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ('id', 'sender', 'created')
        fields = read_only_fields + ('content', 'chat')


class MessageRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        read_only_fields = ('id', 'content', 'sender', 'chat', 'created')
        fields = read_only_fields
