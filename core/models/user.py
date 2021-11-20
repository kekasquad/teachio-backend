import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False
    )
    is_teacher = models.BooleanField(
        verbose_name='Flag if person is a teacher',
        editable=False,
        blank=False,
        null=False,
        default=False
    )
