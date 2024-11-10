# Notification System

## Structural Design Patterns

A simple Python-based Notification System demonstrating three structural design patterns: **Facade**, **Composite**, and **Decorator**.

## Table of Contents

- [Introduction](#introduction)
- [Design Patterns Implemented](#design-patterns-implemented)
  - [Facade Pattern](#facade-pattern)
  - [Composite Pattern](#composite-pattern)
  - [Decorator Pattern](#decorator-pattern)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project extends a Notification System by implementing several **structural design patterns** to improve flexibility, maintainability, and ease of use. The system supports creating and sending different types of notifications, such as Email, SMS, and Push notifications.

### Objectives

1. **Understand and implement structural design patterns**: We applied **Facade**, **Composite**, and **Decorator** patterns to enhance our system.
2. **Enhance the Notification System**: Adding new features using these patterns makes the system more flexible and scalable.
3. **Improve maintainability**: By organizing the codebase and creating simplified interfaces, we make the system more adaptable to future requirements.

## Some Theory

In software engineering, **Structural Design Patterns** focus on the organization and composition of classes and objects. These patterns help with creating larger structures while ensuring flexibility and maintainability. Here are a few common structural design patterns:

- **Facade**
- **Composite**
- **Decorator**
- **Bridge**
- **Flyweight**
- **Adapter**
- **Proxy**

## Design Patterns Implemented

### Facade Pattern

**Purpose**:The Facade Pattern provides a simplified interface to a complex subsystem, hiding the complexities and making it easier to use. The goal is to provide a higher-level interface that makes a system easier to use and understand.

**Implementation**: The `NotificationFacade` class provides a simplified interface for sending Email, SMS, and Push notifications. This hides the complexity of managing different notification types behind a unified method.
Use the Facade Pattern when:

You want to provide a simplified interface to a complex system of objects.
The system has a large number of interdependent classes, and you want to reduce the coupling by abstracting that complexity.
You want to make the system easier to use for the client without exposing the internal workings.

**Structure**
Facade: The class that provides a simplified, unified interface to the complex subsystem. The facade delegates the work to the appropriate classes in the subsystem.
Subsystems: These are the classes that implement the complex logic, which the facade hides. The facade coordinates calls to these subsystems.

```python
# facade/notification_facade.py
from factory.notification_factory import NotificationFactory
from domain.notification_manager import NotificationManager

class NotificationFacade:
    def __init__(self):
        self.manager = NotificationManager()

    def send_email(self, recipient, subject, message, sender_email):
        email = NotificationFactory.create_notification(
            'email', recipient, message, subject=subject, sender_email=sender_email
        )
        self.manager.add_notification(email)
        self.manager.send_all()

    def send_sms(self, recipient, message, phone_number):
        sms = NotificationFactory.create_notification('sms', recipient, message, phone_number=phone_number)
        self.manager.add_notification(sms)
        self.manager.send_all()

    def send_push(self, recipient, message, device_id):
        push = NotificationFactory.create_notification('push', recipient, message, device_id=device_id)
        self.manager.add_notification(push)
        self.manager.send_all()
```

### Usage
```python
# client/main.py
from facade.notification_facade import NotificationFacade

def main():
    facade = NotificationFacade()

    # Sending notifications via the facade
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

if __name__ == "__main__":
    main()
```

## Composite Pattern
**Purpose**: The Composite Pattern is used to treat individual objects and compositions of objects uniformly. This pattern allows you to compose objects into tree-like structures to represent part-whole hierarchies. It is particularly useful when you need to treat groups of objects (composites) in the same way as individual objects.
**Implementation**: Use the Composite Pattern when:

You need to represent part-whole hierarchies.
You want to treat individual objects and their compositions (groups of objects) uniformly.
The structure of objects is hierarchical or tree-like.
For example, in a notification system, you might want to group individual notifications (like email, SMS, or push notifications) into a single composite notification that can be sent as one unit.
**Structure**: 
Component: The interface that both the concrete component and decorators will implement. This defines the operations that can be performed on the objects.
Concrete Component: The original object being decorated, e.g., a basic Notification object.
Decorator: The abstract class that wraps the concrete component and adds additional functionality (e.g., logging, validation).
Concrete Decorators: These are the actual classes that implement the additional behavior. For example, LoggingDecorator or ValidationDecorator can extend the behavior of the Notification object.
```python
# domain/composite_notification.py
from models.notification import Notification

class CompositeNotification(Notification):
    def __init__(self, recipient, message):
        super().__init__(recipient, message)
        self.notifications = []

    def add(self, notification):
        self.notifications.append(notification)

    def remove(self, notification):
        self.notifications.remove(notification)

    def send(self):
        for notification in self.notifications:
            notification.send()  # Delegate sending to each contained notification
```

**Usage**
```python
# client/main.py
from domain.composite_notification import CompositeNotification
from models.email_notification import EmailNotification
from models.sms_notification import SMSNotification
from models.push_notification import PushNotification

def main():
    # Create a composite notification
    composite = CompositeNotification(recipient='Group1', message='Group notification')

    # Add individual notifications to the composite
    composite.add(EmailNotification('john.doe@example.com', 'Group Email', 'Hello, Group!', 'support@example.com'))
    composite.add(SMSNotification('Jane Doe', 'Your group code is 123456.', '+1234567890'))
    composite.add(PushNotification('User123', 'You have a new group message.', 'device_xyz'))

    # Send the composite notification
    composite.send()

if __name__ == "__main__":
    main()
```


## Project Structure
lab2/notification-system/
│
├── client/
│ ├── __init__.py
│ └── main.py # Main script for running the notification system
│
├── domain/
│ ├── __init__.py
│ ├── notification_builder.py # Builder for customizing notifications
│ └── notification_manager.py # Singleton manager for handling notifications
│
├── factory/
│ ├── __init__.py
│ └── notification_factory.py # Factory for creating notifications based on type
│
├── models/
│ ├── __init__.py
│ ├── email_notification.py # Email Notification class
│ ├── notification.py # Base Notification class
│ ├── push_notification.py # Push Notification class
│ └── sms_notification.py # SMS Notification class
│
├── decorators/
│ ├── __init__.py
│ └── logging_decorator.py # Logging decorator for notifications
│
├── tests/
│ ├── __init__.py
│ └── test_singleton.py # Test file for Singleton pattern
│
├── README.md # Project documentation
├── requirements.txt # Project dependencies
└── .gitignore # Git ignore file


## Setup and Installation
git clone https://github.com/dariabriannaa/notification-system.git
cd lab2/notification-system

# Install dependencies
pip install -r requirements.txt

# Running the Application
python3 -m client.main


## Diagram

```mermaid
classDiagram
    direction TB

    %% Facade Pattern
    class NotificationFacade {
        <<Facade>>
        +send_email(recipient, subject, message, sender_email)
        +send_sms(recipient, message, phone_number)
        +send_push(recipient, message, device_id)
    }

    %% Composite Pattern
    class CompositeNotification {
        <<Composite>>
        -notifications: List~Notification~
        +add(notification)
        +remove(notification)
        +send()
    }

    %% Decorator Pattern
    class LoggingDecorator {
        <<Decorator>>
        +send()
    }
    class ValidationDecorator {
        <<Decorator>>
        +send()
    }

    %% Notification Class and Subclasses
    class Notification {
        <<abstract>>
        +recipient: String
        +message: String
        +send()
    }

    class EmailNotification {
        +subject: String
        +sender_email: String
        +send()
    }

    class SMSNotification {
        +phone_number: String
        +send()
    }

    class PushNotification {
        +device_id: String
        +send()
    }

    %% Relationships
    NotificationFacade --> NotificationFactory : "uses"
    NotificationFacade --> NotificationManager : "uses"
    
    NotificationFactory --|> Notification : "creates"
    CompositeNotification --> Notification : "composes"
    
    LoggingDecorator --> Notification : "decorates"
    ValidationDecorator --> Notification : "decorates"
    
    Notification <|-- EmailNotification
    Notification <|-- SMSNotification
    Notification <|-- PushNotification

```

## Conclusion

By implementing structural design patterns like **Facade**, **Composite**, and extending the **Decorator** pattern, we have successfully added flexibility and scalability to the **Notification System**. These patterns allow for:

- **Simplifying the process of interacting with multiple subsystems** (Facade).
- **Organizing complex data structures** (Composite).
- **Dynamically adding functionalities such as logging, validation, or encryption** (Decorator).

These patterns provide a solid foundation for extending the system to handle more complex notification flows or additional features in the future.