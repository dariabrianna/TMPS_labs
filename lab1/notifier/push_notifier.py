from notifier.base_notifier import Notifier

class PushNotifier(Notifier):
    def __init__(self, push_service):
        self.push_service = push_service

    def send(self, device_id, message):
        self.push_service.send(device_id, message)
