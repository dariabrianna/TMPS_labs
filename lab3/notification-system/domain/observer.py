# domain/observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, notification):
        """Receive and handle a notification."""
        pass
