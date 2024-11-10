from models.notification import Notification

class CompositeNotification(Notification):
    def __init__(self, recipient, message):
        super().__init__(recipient, message)
        self.notifications = []

    def add(self, notification):
        self.notifications.append(notification)

    def remove(self, notification):
        self.notifications.remove(notification)

    def send(self):
        for notification in self.notifications:
            notification.send()
