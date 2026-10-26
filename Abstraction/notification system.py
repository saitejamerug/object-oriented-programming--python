# Create an abstract class Notification with:
#     send(message)
#     create:
#     Email
#     SMS
#     Whatsapp

from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
class Email(Notification):
    def send(self, message):
        print("Sending Email", message, "from Email")
class SMS(Notification):
    def send(self, message):
        print("Sending message", message, "from SMS ")
class Whatsapp(Notification):
    def send(self, message):
        print("Sending message", message, "from Whatsapp")
email = Email()
email.send("Hello!")

sms = SMS()
sms.send("What are you doing?")

whatsapp = Whatsapp()
whatsapp.send("How are you?")