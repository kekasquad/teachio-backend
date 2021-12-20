from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification


def send_notification(user_id, title, message, data=None):
    try:
        device = FCMDevice.objects.filter(user_id=user_id, active=True).first()
        result = device.send_message(
            Message(
                data=data,
                notification=Notification(
                    title=title,
                    body=message
                ))
        )
        return result
    except:
        pass
