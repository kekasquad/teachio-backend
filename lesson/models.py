import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel


class Lesson(TimeStampedModel):
    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    class PaymentStatus(models.TextChoices):
        NOT_CONFIRMED = 'NotConfirmed', _('NotConfirmed')
        REQUESTED = 'Requested', _('Requested')
        CONFIRMED = 'Confirmed', _('Confirmed')

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
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
    homework = models.TextField(
        max_length=1000,
        blank=True,
        null=True
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
    cost = models.IntegerField(
        null=False,
        blank=False,
    )
    payment_status = models.CharField(
        max_length=30,
        choices=PaymentStatus.choices,
        null=False,
        blank=False,
        default=PaymentStatus.NOT_CONFIRMED
    )

    def get_status(self) -> PaymentStatus:
        return self.PaymentStatus[self.payment_status]
