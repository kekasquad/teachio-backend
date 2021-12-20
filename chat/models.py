import uuid

from django.db import models
from django.contrib import admin

from core.models import TimeStampedModel


class Chat(TimeStampedModel):
    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'chats'
        unique_together = (('student', 'teacher'),)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    student = models.ForeignKey(
        'core.User',
        related_name='student_chats',
        on_delete=models.CASCADE,
    )
    teacher = models.ForeignKey(
        'core.User',
        related_name='teacher_chats',
        on_delete=models.CASCADE
    )
    teacher_unread = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
    student_unread = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )


admin.site.register(Chat)
