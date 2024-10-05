from models.email_notification import EmailNotification
from models.sms_notification import SMSNotification
from models.push_notification import PushNotification

class NotificationBuilder:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.notification_type = None
        self.extra_params = {}

    def set_recipient(self, recipient):
        self.recipient = recipient
        return self

    def set_message(self, message):
        self.message = message
        return self

    def set_notification_type(self, notification_type):
        self.notification_type = notification_type
        return self

    def set_extra_param(self, key, value):
        self.extra_params[key] = value
        return self

    def build(self):
        if not self.notification_type:
            raise ValueError("Notification type must be set.")
        if not self.recipient or not self.message:
            raise ValueError("Recipient and message must be set.")
        
        if self.notification_type == 'email':
            return EmailNotification(self.recipient, self.message, 
                                     self.extra_params.get('subject', 'No Subject'), 
                                     self.extra_params.get('sender_email', 'no-reply@example.com'))
        elif self.notification_type == 'sms':
            return SMSNotification(self.recipient, self.message, 
                                   self.extra_params.get('phone_number', '0000000000'))
        elif self.notification_type == 'push':
            return PushNotification(self.recipient, self.message, 
                                    self.extra_params.get('device_id', 'unknown_device'))
        else:
            raise ValueError(f"Unknown notification type: {self.notification_type}")
