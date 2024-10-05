import unittest
from domain.notification_manager import NotificationManager

class TestNotificationManagerSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        manager1 = NotificationManager()
        manager2 = NotificationManager()
        self.assertIs(manager1, manager2, "NotificationManager instances are not the same (Singleton failed).")

    def test_add_notification(self):
        manager = NotificationManager()
        manager.notifications = []  # Reset notifications for test
        manager.add_notification("Test Notification")
        self.assertIn("Test Notification", manager.notifications)

if __name__ == '__main__':
    unittest.main()
