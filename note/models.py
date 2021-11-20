import uuid

from django.db import models


class Note(models.Model):

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
