# domain/sms_notifier.py

from domain.observer import Observer
from models.sms_notification import SMSNotification

class SMSNotifier(Observer):
    def update(self, notification):
        if isinstance(notification, SMSNotification):
            notification.send()
