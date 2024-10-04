# main.py

from notifier.email_notifier import EmailNotifier
from notifier.sms_notifier import SMSNotifier
from notifier.push_notifier import PushNotifier
from services.email_service import EmailService
from services.sms_service import SMSService
from services.push_service import PushService

def main():
    # Initialize services
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PushService()

    # Initialize notifiers with their respective services
    email_notifier = EmailNotifier(email_service)
    sms_notifier = SMSNotifier(sms_service)
    push_notifier = PushNotifier(push_service)

    # Sending notifications
    # Adjusted to pass only recipient and message
    email_notifier.send("user@example.com", "Thank you for signing up!")
    sms_notifier.send("+1234567890", "Your verification code is 1234.")
    push_notifier.send("device123", "You have a new message.")

if __name__ == "__main__":
    main()
