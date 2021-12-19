from fcm_django.models import FCMDevice


def send_notification(user_ids,title, message, data):
   try:
      device = FCMDevice.objects.filter(user__in=user_ids).first()
      result = device.send_message(
          title=title,
          body=message,
          data=data,
          sound=True
      )
      return result
   except:
      pass