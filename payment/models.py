import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel


class Payment(TimeStampedModel):

    class Status(models.TextChoices):
        NOT_CONFIRMED = 'NotConfirmed', _('NotConfirmed')
        REQUESTED = 'Requested', _('Requested')
        CONFIRMED = 'Confirmed', _('Confirmed')

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    cost = models.IntegerField(
        null=False,
        blank=False,
    )
    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        null=False,
        blank=False,
        default=Status.NOT_CONFIRMED
    )

    def get_status(self) -> Status:
        return self.Status[self.status]