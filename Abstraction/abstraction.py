from abc import ABC, abstractmethod
class Whatsapp(ABC):
    @abstractmethod
    def send(self):
        pass

class SendPhoto(Whatsapp):
    def send(self):
        print("Compressing Image..")
        print("Encrypting Image..")
        print("Decrypting Image..")
        print("Image sent!")

class SendText(Whatsapp):
    def send(self):
        print("Encrypting text..")
        print("Decrypting text..")
        print("Text sent!")

photo = SendPhoto()
photo.send()
print()
text = SendText()
text.send()
