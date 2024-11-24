# domain/push_notifier.py

from domain.observer import Observer
from models.push_notification import PushNotification

class PushNotifier(Observer):
    def update(self, notification):
        if isinstance(notification, PushNotification):
            notification.send()
