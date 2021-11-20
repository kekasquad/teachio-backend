import uuid

from django.db import models

from core.models import TimeStampedModel


class Note(TimeStampedModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        null=False,
    )
    content = models.TextField(
        max_length=500,
        null=False,
        blank=False,
    )
