# Notification System

A simple Python-based Notification System demonstrating three creational design patterns: **Factory Method**, **Singleton**, and **Builder**.

## Table of Contents

- [Introduction](#introduction)
- [Design Patterns Implemented](#design-patterns-implemented)
  - [Factory Method](#factory-method)
  - [Singleton](#singleton)
  - [Builder](#builder)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases how to implement common creational design patterns in Python within a simple Notification System. The system supports creating and sending different types of notifications, such as Email, SMS, and Push notifications, each of which is handled through different design patterns to illustrate their practical use.

## Design Patterns Implemented

### Factory Method

**Purpose:** Defines an interface for creating an object but allows subclasses to alter the type of objects that will be created.

**Implementation:** The NotificationFactory class in the factory module provides a static method, create_notification, which returns an instance of EmailNotification, SMSNotification, or PushNotification based on the notification_type parameter. This approach allows for easy extensibility—if you want to add new notification types in the future, you just need to add a new class for the notification type and update the factory method without modifying existing code.

**Snippet**

```# factory/notification_factory.py

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type, recipient, message, **kwargs):
        if notification_type == 'email':
            return EmailNotification(recipient, message, kwargs.get('subject', 'No Subject'), kwargs.get('sender_email', 'no-reply@example.com'))
        elif notification_type == 'sms':
            return SMSNotification(recipient, message, kwargs.get('phone_number'))
        elif notification_type == 'push':
            return PushNotification(recipient, message, kwargs.get('device_id'))
        else:
            raise ValueError(f"Unknown type: {notification_type}")
```

**Usage**

```# Create an Email Notification
email = NotificationFactory.create_notification(
    'email', 'user@example.com', 'Welcome!', subject='Greetings', sender_email='support@example.com'
)

# Send the notification
email.send()
```

### Singleton

**Purpose:** Ensures a class has only one instance and provides a global point of access to it.

**Implementation:** The Singleton pattern ensures a class has only one instance. This is used in the NotificationManager class so that all notifications are managed by one central instance.

**Snippet**:

```class NotificationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.notifications = []
        return cls._instance
```

### Builder

**Purpose:** Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

**Implementation:** The Builder pattern is useful for creating objects step-by-step with optional fields. The NotificationBuilder class lets us create a notification and add extra fields only if needed.

**Snippet**

```# domain/notification_builder.py

class NotificationBuilder:
    def __init__(self):
        self.notification_data = {}

    def set_recipient(self, recipient):
        self.notification_data['recipient'] = recipient
        return self

    def set_message(self, message):
        self.notification_data['message'] = message
        return self

    def set_notification_type(self, notification_type):
        self.notification_data['type'] = notification_type
        return self

    def set_extra_param(self, key, value):
        self.notification_data[key] = value
        return self

    def build(self):
        if self.notification_data['type'] == 'email':
            return EmailNotification(self.notification_data['recipient'], self.notification_data['message'],
                                     self.notification_data.get('subject', 'No Subject'))
        elif self.notification_data['type'] == 'sms':
            return SMSNotification(self.notification_data['recipient'], self.notification_data['message'])
        else:
            raise ValueError("Invalid notification type")
```

**Usage**:

```from domain.notification_builder import NotificationBuilder

builder = NotificationBuilder()
email_notification = (builder
                      .set_recipient('user@example.com')
                      .set_message('Your order has shipped!')
                      .set_notification_type('email')
                      .set_extra_param('subject', 'Shipping Update')
                      .set_extra_param('sender_email', 'orders@example.com')
                      .build())
```

## Project Structure

lab2/notification-system/
│
├── client/
│ ├── **init**.py
│ └── main.py # Main script for running the notification system
│
├── domain/
│ ├── **init**.py
│ ├── notification_builder.py # Builder for customizing notifications
│ └── notification_manager.py # Singleton manager for handling notifications
│
├── factory/
│ ├── **init**.py
│ └── notification_factory.py # Factory for creating notifications based on type
│
├── models/
│ ├── **init**.py
│ ├── email_notification.py # Email Notification class
│ ├── notification.py # Base Notification class
│ ├── push_notification.py # Push Notification class
│ └── sms_notification.py # SMS Notification class
│
├── tests/
│ ├── **init**.py
│ └── test_singleton.py # Test file for Singleton pattern
│
├── README.md # Project documentation
├── requirements.txt # Project dependencies
└── .gitignore # Git ignore file

**Description**
The project is structured into several modules:

- `client`: The main entry point for the notification system.
- `domain`: Contains classes related to the domain logic, such as the NotificationManager and NotificationBuilder
- `factory`: Contains the factory for creating notifications based on type
- `models`: Contains the base Notification class and its concrete implementations (EmailNotification, PushNotification,
- `tests`: Holds unit tests for validating the functionality of the system, including the Singleton pattern.
- `README.md`: Project documentation
- `main`: Entry point of the application.

## Setup and Installation

### Clone the Repository:

```bash
git clone https://github.com/dariabriannaa/notification-system.git
cd lab2/notification-system

Install dependecies
pip install -r requirements.txt

Running the Application
python3 -m client.main


```
