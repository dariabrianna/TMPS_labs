# Notification System

## Creational Design Patterns

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

## Objectives

1. Study and understand the Creational Design Patterns.

2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.

3. Use some creational design patterns for object instantiation in a sample project.

## Some Theory

In software engineering, the creational design patterns are the general solutions that deal with object creation, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by optimizing, hiding or controlling the object creation.

Some examples of this kind of design patterns are:

- Singleton
- Builder
- Prototype
- Object Pooling
- Factory Method
- Abstract Factory

## Main Tasks

1. Choose an OO programming language and a suitable IDE or Editor (No frameworks/libs/engines allowed).

2. Select a domain area for the sample project.

3. Define the main involved classes and think about what instantiation mechanisms are needed.

4. Based on the previous point, implement atleast 3 creational design patterns in your project.

## Features

- **Flexible Notification Creation**: Supports creating Email, SMS, and Push notifications with easy extensibility for new types.
- **Design Patterns Implemented**:
  - **Factory Method** for dynamic creation of notification types.
  - **Singleton** to ensure a single instance of `NotificationManager` for managing notifications.
  - **Builder** to allow for customized notification construction.
- **Centralized Notification Management**: Manages and dispatches notifications from a central manager (`NotificationManager`).
- **Easily Extendable**: Add new notification types by creating a class and updating the factory without modifying core logic.
- **Unit Testing**: Includes unit tests to ensure that each component works as expected.

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

### Diagram

```mermaid
classDiagram
    direction TB

    class NotificationManager {
        <<Singleton>>
        -notifications: List~Notification~
        +add_notification(notification)
        +send_all()
    }

    class NotificationFactory {
        <<Factory Method>>
        +create_notification(type, recipient, message, extras)
    }

    class NotificationBuilder {
        <<Builder>>
        +set_recipient(recipient)
        +set_message(message)
        +set_notification_type(type)
        +set_extra_param(key, value)
        +build() Notification
    }

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

    %% Relationships %%
    NotificationManager o-- Notification : "manages"
    NotificationManager ..> NotificationFactory : "uses"
    NotificationManager ..> NotificationBuilder : "uses"

    NotificationFactory --|> Notification : "creates"
    NotificationBuilder --|> Notification : "builds"

    Notification <|-- EmailNotification
    Notification <|-- SMSNotification
    Notification <|-- PushNotifications