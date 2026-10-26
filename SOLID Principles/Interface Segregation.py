# Interface Segregation: No class should be forced to Implement the method it doesn't need
from abc import ABC, abstractmethod
class Phone(ABC):
    @abstractmethod
    def call(self):
        pass
    @abstractmethod
    def msg(self):
        pass
    @abstractmethod
    def cam(self):
        pass
    @abstractmethod
    def bluetooth(self):
        pass
    @abstractmethod
    def volume_control(self):
        pass

class SplitScreen:
    def splitscreen(self):
        pass

class Airdrop:
    def airdrop(self):
        pass

class Android(Phone, SplitScreen):
    def call(self):
        print("Calling..")
    def msg(self):
        print("Messaging..")
    def cam(self):
        print("Opening Camera..")
    def bluetooth(self):
        print("Turning On Bluetooth..")
    def volume_control(self):
        print("Controlling volume..")
    def splitscreen(self):
        print("Splitting Screen..")

class Iphone(Phone, Airdrop):
    def call(self):
        print("Calling..")
    def msg(self):
        print("Messaging..")
    def cam(self):
        print("Opening Camera..")
    def bluetooth(self):
        print("Turning on Bluetooth..")
    def volume_control(self):
        print("Controlling volume..")
    def airdrop(self):
        print("Air dropping screen..")

android = Android()
iphone = Iphone()

android.splitscreen()
iphone.airdrop()