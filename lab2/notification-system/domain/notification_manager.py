class NotificationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls)
            cls._instance.notifications = []
        return cls._instance

    def add_notification(self, notification):
        self.notifications.append(notification)

    def send_all(self):
        for notification in self.notifications:
            notification.send()
        self.notifications.clear()
