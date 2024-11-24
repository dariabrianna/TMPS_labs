# domain/notification_manager.py
from domain.email_notifier import EmailNotifier
from domain.sms_notifier import SMSNotifier
from domain.push_notifier import PushNotifier

class NotificationManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.notifications = []
            cls._instance.observers = []
        return cls._instance

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, notification):
        for observer in self.observers:
            observer.update(notification)

    def add_notification(self, notification):
        self.notifications.append(notification)
        self.notify_observers(notification)
