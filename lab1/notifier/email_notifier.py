from notifier.base_notifier import Notifier 

class EmailNotifier(Notifier):
    def __init__(self, email_service):
        self.email_service = email_service

    def send(self, recipient, message):
        subject = "Notification"
        self.email_service.send(recipient, subject, message)
