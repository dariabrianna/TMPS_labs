from .notification import Notification

class PushNotification(Notification):
    def __init__(self, recipient, message, device_id):
        super().__init__(recipient, message)
        self.device_id = device_id

    def send(self):
        print(f"Sending Push Notification to device {self.device_id}")
        print(f"Message: {self.message}\n")
