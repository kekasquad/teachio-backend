import logging
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from notification.fcm import send_notification
from .models import Message

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Message)
def message_create_update_receiver(created, instance, **_):
    logger.info(f"Post-save Message: ${created} ${instance!r}")
    if created:
        #         with transaction.atomic():
        #             if instance.sender.is_teacher:
        #                 instance.chat.student_unread += 1
        #             else:
        #                 instance.chat.teacher_unread += 1
        #             instance.chat.save()

        if instance.sender.is_teacher:
            send_notification(
                str(instance.chat.student.id),
                f'New message from {instance.sender.get_full_name()}',
                f'You have unread messages',
                {
                    'chat_id': str(instance.chat.id)
                }
            )
        else:
            send_notification(
                str(instance.chat.teacher.id),
                f'New message from {instance.sender.get_full_name()}',
                f'You have unread messages',
                {
                    'chat_id': str(instance.chat.id)
                }
            )
