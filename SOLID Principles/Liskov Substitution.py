# Liskov Substitution Principle: A child class must behave correctly when used in place of its parent class.
class Message:
    def send(self):
        pass
class Text(Message):
    def send(self):
        print("Sending Text..")
class Image(Message):
    def send(self):
        print("Sending Image..")

def deliver(message):
    message.send()
deliver(Text())
deliver(Image())
deliver(Message())