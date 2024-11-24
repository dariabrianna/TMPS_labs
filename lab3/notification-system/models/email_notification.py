from .notification import Notification

class EmailNotification(Notification):
    def __init__(self, recipient, message, subject, sender_email):
        super().__init__(recipient, message)
        self.subject = subject
        self.sender_email = sender_email

    def send(self):
        print(f"Sending Email to {self.recipient}")
        print(f"From: {self.sender_email}")
        print(f"Subject: {self.subject}")
        print(f"Message: {self.message}\n")
