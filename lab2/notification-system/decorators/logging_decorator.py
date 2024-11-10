# decorators/logging_decorator.py

class LoggingDecorator:
    def __init__(self, notification):
        self._notification = notification  # The notification object to be decorated

    def send(self):
        # Log before sending the notification
        print(f"Logging: Sending {self._notification.__class__.__name__} to {self._notification.recipient}")
        
        # Call the send method of the actual notification object
        self._notification.send()
