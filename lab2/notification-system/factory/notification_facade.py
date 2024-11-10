from domain.notification_manager import NotificationManager
from factory.notification_factory import NotificationFactory

class NotificationFacade:
    def __init__(self):
        self.manager = NotificationManager()

    def send_email(self, recipient, subject, message, sender_email):
        email = NotificationFactory.create_notification('email', recipient, message, subject=subject, sender_email=sender_email)
        self.manager.add_notification(email)
        self.manager.send_all()

    def send_sms(self, recipient, message, phone_number):
        sms = NotificationFactory.create_notification('sms', recipient, message, phone_number=phone_number)
        self.manager.add_notification(sms)
        self.manager.send_all()

    def send_push(self, recipient, message, device_id):
        push = NotificationFactory.create_notification('push', recipient, message, device_id=device_id)
        self.manager.add_notification(push)
        self.manager.send_all()
