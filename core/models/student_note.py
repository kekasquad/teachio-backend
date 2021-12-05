from django.db import models


class StudentNote(models.Model):
    class Meta:
        unique_together = (('student', 'teacher'),)
        index_together = (('student', 'teacher'),)

    teacher = models.ForeignKey(
        'core.User',
        related_name='students_notes',
        on_delete=models.CASCADE,
        null=False,
    )
    student = models.ForeignKey(
        'core.User',
        related_name='student_students_notes',
        on_delete=models.CASCADE,
        null=False,
    )
    description = models.TextField(
        max_length=500,
        null=False,
        blank=True,
    )
