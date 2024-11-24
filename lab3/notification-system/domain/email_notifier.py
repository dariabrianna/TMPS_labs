# domain/email_notifier.py

from domain.observer import Observer
from models.email_notification import EmailNotification

class EmailNotifier(Observer):
    def update(self, notification):
        if isinstance(notification, EmailNotification):
            notification.send()
