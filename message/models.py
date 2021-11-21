import uuid

from django.db import models

from core.models import TimeStampedModel


class Message(TimeStampedModel):
    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    content = models.TextField(
        max_length=255,
        blank=False,
        null=False
    )
    sender = models.ForeignKey(
        'core.User',
        related_name='sender',
        on_delete=models.DO_NOTHING
    )
    chat = models.ForeignKey(
        'chat.Chat',
        related_name='chat',
        on_delete=models.CASCADE
    )