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

This project showcases how to implement common creational design patterns in Python within a simple Notification System. The system supports creating and sending different types of notifications: Email, SMS, and Push.


## Design Patterns Implemented

### Factory Method

**Purpose:** Defines an interface for creating an object but allows subclasses to alter the type of objects that will be created.

**Implementation:** `NotificationFactory` class in the `factory` module creates instances of different notification types based on input parameters.

### Singleton

**Purpose:** Ensures a class has only one instance and provides a global point of access to it.

**Implementation:** `NotificationManager` class in the `domain` module ensures only one instance manages all notifications.

### Builder

**Purpose:** Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

**Implementation:** `NotificationBuilder` class in the `domain` module allows step-by-step construction of notification objects with optional parameters.

## Project Structure

