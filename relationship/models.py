from django.db import models

from core.models import TimeStampedModel


class Relationship(TimeStampedModel):
    class Meta:
        verbose_name = 'relationship'
        verbose_name_plural = 'relationships'
        unique_together = (('student', 'teacher'),)
        index_together = (('student', 'teacher'),)

    student = models.ForeignKey(
        'core.User',
        related_name='student_relationship',
        on_delete=models.CASCADE,
    )
    teacher = models.ForeignKey(
        'core.User',
        related_name='teacher_relationship',
        on_delete=models.CASCADE
    )
