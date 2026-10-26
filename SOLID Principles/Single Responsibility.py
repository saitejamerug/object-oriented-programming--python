# Single Responsibility you shouldn't assign multiple responsibilities to a single class
from abc import ABC, abstractmethod
class Netflix(ABC):
    @abstractmethod
    def execute(self):
        pass

class Contents(Netflix):
    def execute(self):
        print("Managing movies and web series")

class Payments(Netflix):
    def execute(self):
        print("processing subscription payments")

class Notifications(Netflix):
    def execute(self):
        print("sending subscription notifications")

content = Contents()
payment = Payments()
notifications = Notifications()

content.execute()
payment.execute()
notifications.execute()