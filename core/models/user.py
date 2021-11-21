import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False
    )
    email = models.EmailField(
        _('email address'),
        db_index=True,
        unique=True,
        blank=False,
        null=False,
    )
    is_teacher = models.BooleanField(
        verbose_name='Flag if person is a teacher',
        editable=False,
        blank=False,
        null=False,
        default=False
    )
