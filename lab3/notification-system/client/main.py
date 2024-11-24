import sys
import os

# Add the project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from factory.notification_factory import NotificationFactory
from domain.notification_manager import NotificationManager
from domain.notification_builder import NotificationBuilder
from domain.email_notifier import EmailNotifier
from domain.sms_notifier import SMSNotifier
from domain.push_notifier import PushNotifier

def main():
    # Create the NotificationManager (Singleton)
    manager = NotificationManager()

    # Register observers
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()
    push_notifier = PushNotifier()

    manager.register_observer(email_notifier)
    manager.register_observer(sms_notifier)
    manager.register_observer(push_notifier)

    # Using Factory Method to create notifications
    email = NotificationFactory.create_notification(
        'email',
        recipient='john.doe@example.com',
        message='Welcome to our service!',
        subject='Welcome!',
        sender_email='support@example.com'
    )
    
    sms = NotificationFactory.create_notification(
        'sms',
        recipient='Jane Doe',
        message='Your verification code is 123456.',
        phone_number='+1234567890'
    )
    
    push = NotificationFactory.create_notification(
        'push',
        recipient='User123',
        message='You have a new friend request.',
        device_id='device_xyz'
    )

    # Adding notifications to the manager
    manager.add_notification(email)  # Observers are notified
    manager.add_notification(sms)   # Observers are notified
    manager.add_notification(push)  # Observers are notified

    # Using Builder to create a custom notification
    builder = NotificationBuilder()
    custom_email = (builder
                    .set_recipient('alice@example.com')
                    .set_message('Your order has been shipped!')
                    .set_notification_type('email')
                    .set_extra_param('subject', 'Order Shipped')
                    .set_extra_param('sender_email', 'orders@example.com')
                    .build())
    
    manager.add_notification(custom_email)  # Observers are notified

    # Notifications are sent automatically by observers; no need to call `send_all()` here

if __name__ == "__main__":
    main()
