from django.db.models.signals import post_save
from django.dispatch import receiver

from notification.fcm import send_notification
from .models import Lesson


@receiver(post_save, sender=Lesson)
def lesson_create_update_receiver(sender, instance, created, **kwargs):
    if created:
        send_notification(
            str(instance.student.id),
            'New lesson',
            f'Lesson {instance.title} created by your teacher {instance.teacher.get_full_name()}!',
            {
                'lesson_id': str(instance.id),
            }
        )
    elif (
            'payment_status' in (kwargs.get('update_fields') or set()) and
            instance.payment_status == Lesson.PaymentStatus.REQUESTED
    ):
        send_notification(
            str(instance.teacher.id),
            'Payment confirmation',
            f'Your student {instance.student.get_full_name()} requests confirmation for '
            f'the lesson {instance.title}',
            {
                'lesson_id': str(instance.id),
            }
        )
    else:
        send_notification(
            str(instance.student.id),
            'Lesson updated',
            f'Lesson {instance.title} changed by your teacher '
            f'{instance.teacher.get_full_name()}, check for updates now',
            {
                'lesson_id': str(instance.id),
            }
        )
