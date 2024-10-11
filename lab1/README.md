# Notification System

This project demonstrates the implementation of two SOLID principles using a simple notification system. The system supports multiple types of notifications: Email, SMS, and Push Notifications. Each notification type adheres to the Single Responsibility Principle (SRP) and Open/Closed Principle (OCP) from the SOLID design principles.

## Project Structure

# Notification System - SOLID Principles Implementation

## Laboratory Work 1

### Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [SOLID Principles Applied](#solid-principles-applied)
  - [Single Responsibility Principle (SRP)](#single-responsibility-principle-srp)
  - [Open/Closed Principle (OCP)](#openclosed-principle-ocp)
- [Project Structure](#project-structure)
  - [Directory Breakdown](#directory-breakdown)
  - [Class Diagram](#class-diagram)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Example Output](#example-output)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contribution](#contribution)
- [License](#license)
- [Author](#author)

---

## Introduction

Welcome to the **Notification System** project, developed as part of Laboratory Work 1. This project showcases the practical application of two key **SOLID principles**—**Single Responsibility Principle (SRP)** and **Open/Closed Principle (OCP)**—to build a maintainable, scalable, and robust notification system. The system is designed to send notifications through various channels such as **Email**, **SMS**, and **Push Notifications**.

---

## Features

- **Email Notifications**: Send personalized emails with customizable subjects and messages.
- **SMS Notifications**: Dispatch SMS messages to specified phone numbers.
- **Push Notifications**: Deliver push notifications to designated device IDs.
- **Extensibility**: Easily add new notification channels (e.g., Slack, WhatsApp) without modifying existing code.
- **Modularity**: Each component has a well-defined responsibility, enhancing code readability and maintainability.
- **Logging**: Integrated logging for monitoring and debugging purposes.
- **Configuration Management**: Centralized configuration using environment variables for flexibility across different environments.

---

## SOLID Principles Applied

### Single Responsibility Principle (SRP)

**Definition:**  
A class should have only one reason to change, meaning it should have only one job or responsibility.

**Implementation in the Project:**

- **Notifier Classes**: Each notifier class (`EmailNotifier`, `SMSNotifier`, `PushNotifier`) is responsible solely for sending notifications through its respective channel.
- **Service Classes**: Each service class (`EmailService`, `SMSService`, `PushService`) handles the actual logic of sending notifications, such as integrating with external APIs or handling message formatting.
- **Logger**: A dedicated `Logger` class manages all logging functionalities, ensuring that logging concerns are separated from business logic.

**Benefits:**

- Enhances maintainability by isolating changes to specific components.
- Simplifies debugging and testing by focusing on individual responsibilities.

### Open/Closed Principle (OCP)

**Definition:**  
Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

**Implementation in the Project:**

- **Abstract Base Class**: An abstract `Notifier` base class defines a common interface for all notifier types.
- **Extensible Notifier Classes**: New notifier types can be added by creating new classes that inherit from the `Notifier` base class without altering existing notifier classes.
  
**Example:**

To add a new **SlackNotifier**, simply create a new class that inherits from `Notifier` and implements the `send` method.

**Benefits:**

- Facilitates scalability by allowing the addition of new features without impacting existing functionality.
- Reduces the risk of introducing bugs when extending the system.

---

## Project Structure

### Directory Breakdown

notification_system/ ├── notifier/ │ ├── init.py │ ├── base_notifier.py │ ├── email_notifier.py │ ├── sms_notifier.py │ └── push_notifier.py ├── services/ │ ├── init.py │ ├── email_service.py │ ├── sms_service.py │ └── push_service.py ├── utils/ │ ├── init.py │ └── logger.py ├── config/ │ ├── init.py │ └── config.py ├── tests/ │ ├── init.py │ ├── test_email_notifier.py │ ├── test_sms_notifier.py │ └── test_push_notifier.py ├── main.py ├── requirements.txt └── README.md


**Description:**

- **notifier/**: Contains notifier classes adhering to SRP and OCP.
- **services/**: Houses service classes responsible for the actual sending logic.
- **utils/**: Includes utility modules like logging.
- **config/**: Manages configuration settings, possibly using environment variables.
- **tests/**: Contains unit tests for notifier classes.
- **main.py**: Entry point of the application.
- **requirements.txt**: Lists project dependencies.
- **README.md**: Project documentation.

### Class Diagram

Below is a UML class diagram illustrating the relationships between the classes in the project. This diagram uses [Mermaid](https://mermaid-js.github.io/) syntax, which is supported by many Markdown editors, including VS Code with the appropriate extensions.

```mermaid
classDiagram
    direction TB

    class Notifier {
        <<abstract>>
        +send(recipient, message)
    }

    class EmailNotifier {
        +send(recipient, subject, message)
    }

    class SMSNotifier {
        +send(phone_number, message)
    }

    class PushNotifier {
        +send(device_id, message)
    }

    class EmailService {
        +send(recipient, subject, message)
    }

    class SMSService {
        +send(phone_number, message)
    }

    class PushService {
        +send(device_id, message)
    }

    class Logger {
        +log(message)
    }

    Notifier <|-- EmailNotifier
    Notifier <|-- SMSNotifier
    Notifier <|-- PushNotifier

    EmailNotifier --> EmailService
    SMSNotifier --> SMSService
    PushNotifier --> PushService

    EmailNotifier --> Logger
    SMSNotifier --> Logger
    PushNotifier --> Logger

