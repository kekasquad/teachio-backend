from django.db import models


class ActivationCode(models.Model):
    user = models.ForeignKey(
        'core.User',
        related_name='activation_code',
        on_delete=models.CASCADE,
        null=False,
    )
    code = models.CharField(
        max_length=4,
        null=False,
        blank=False,
    )
