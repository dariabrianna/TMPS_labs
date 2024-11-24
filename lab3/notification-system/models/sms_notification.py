from .notification import Notification

class SMSNotification(Notification):
    def __init__(self, recipient, message, phone_number):
        super().__init__(recipient, message)
        self.phone_number = phone_number

    def send(self):
        print(f"Sending SMS to {self.phone_number}")
        print(f"Message: {self.message}\n")
