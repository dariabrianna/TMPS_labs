class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        raise NotImplementedError("Subclasses must implement the send method.")
