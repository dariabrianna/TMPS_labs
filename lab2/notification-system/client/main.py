import sys
import os

# Add the project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from factory.notification_factory import NotificationFactory
from factory.notification_facade import NotificationFacade
from domain.composite_notification import CompositeNotification
from models.email_notification import EmailNotification
from models.sms_notification import SMSNotification
from models.push_notification import PushNotification
from decorators.logging_decorator import LoggingDecorator

def main():
    # Use the NotificationFacade to send notifications easily
    facade = NotificationFacade()

    # Sending notifications via the facade with logging
    facade.send_email(
        recipient='john.doe@example.com',
        subject='Welcome!',
        message='Welcome to our service!',
        sender_email='support@example.com'
    )
    
    facade.send_sms(
        recipient='Jane Doe',
        message='Your verification code is 123456.',
        phone_number='+1234567890'
    )
    
    facade.send_push(
        recipient='User123',
        message='You have a new friend request.',
        device_id='device_xyz'
    )

    # CompositeNotification: Grouping multiple notifications together
    composite = CompositeNotification(recipient='Group1', message='Group notification')

    # Add individual notifications to the composite, decorated with logging
    composite.add(LoggingDecorator(EmailNotification('john.doe@example.com', 'Group Email', 'Hello, Group!', 'support@example.com')))
    composite.add(LoggingDecorator(SMSNotification('Jane Doe', 'Your group code is 123456.', '+1234567890')))
    composite.add(LoggingDecorator(PushNotification('User123', 'You have a new group message.', 'device_xyz')))

    # Send the composite notification with logging
    composite.send()

if __name__ == "__main__":
    main()
