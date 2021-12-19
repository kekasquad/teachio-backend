from django.db.models.signals import post_save
from django.dispatch import receiver

from notification.fcm import send_notification
from .models import Lesson


@receiver(post_save, sender=Lesson)
def lesson_create_update_receiver(created, instance, **_):
    if created:
        send_notification(
            instance.student,
            'New lesson',
            f'Lesson {instance.title} created by your teacher {instance.teacher.get_full_name()}!',
            {
                'lesson_id': instance.id,
            }
        )
    else:
        send_notification(
            instance.student,
            'Lesson updated',
            f'Lesson {instance.title} changed by your teacher '
            f'{instance.teacher.get_full_name()}, check for updates now',
            {
                'lesson_id': instance.id,
            }
        )
