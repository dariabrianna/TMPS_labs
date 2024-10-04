from notifier.base_notifier import Notifier

class SMSNotifier(Notifier):
    def __init__(self, sms_service):
        self.sms_service = sms_service

    def send(self, phone_number, message):
        self.sms_service.send(phone_number, message)
