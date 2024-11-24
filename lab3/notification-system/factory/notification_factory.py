from models.email_notification import EmailNotification
from models.sms_notification import SMSNotification
from models.push_notification import PushNotification

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type, recipient, message, **kwargs):
        if notification_type == 'email':
            return EmailNotification(recipient, message, kwargs.get('subject'), kwargs.get('sender_email'))
        elif notification_type == 'sms':
            return SMSNotification(recipient, message, kwargs.get('phone_number'))
        elif notification_type == 'push':
            return PushNotification(recipient, message, kwargs.get('device_id'))
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
