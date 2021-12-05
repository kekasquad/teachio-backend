import secrets

from django.core.mail import send_mail

from core.models import User
from core.models import ActivationCode


def send_code(user: User):
    code = secrets.randbelow(9000) + 1000
    ActivationCode.objects.update_or_create(
        user=user,
        defaults={'code': code}
    )

    send_mail(
        'Verify your account',
        f'Here is your code for verification: {code}\nTeach.io',
        'noreply@teach.io',
        [user.email],
        fail_silently=False,
    )
