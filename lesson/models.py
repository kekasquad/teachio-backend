import uuid

from django.db import models

from core.models import TimeStampedModel


class Lesson(TimeStampedModel):
    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        db_index=True
    )
    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )
    start = models.DateTimeField(
        blank=False,
        null=False,
    )
    end = models.DateTimeField(
        blank=False,
        null=False,
    )
    student = models.ForeignKey(
        'core.User',
        related_name='student_lessons',
        on_delete=models.CASCADE,
    )
    teacher = models.ForeignKey(
        'core.User',
        related_name='teacher_lessons',
        on_delete=models.CASCADE
    )
