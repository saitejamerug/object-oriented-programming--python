# Create an abstract class Payment with an abstract method pay(amount)
# UPI
# CreditCard
# Cash

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(Payment):
    def __init__(self, balance):
        self.balance = balance
    def pay(self, amount):
        print("Payment successful of Rs.",amount)

class CreditCard(Payment):
    def __init__(self, balance):
        self.balance = balance
    def pay(self, amount):
        print("Payment successful of Rs.",amount)

class Cash(Payment):
    def __init__(self, balance):
        self.balance = balance
    def pay(self, amount):
        print("Payment Successful of Rs.",amount)
upi = UPI(25000)
upi.pay(5000)
print()
creditcard = CreditCard(25000)
creditcard.pay(5000)
print()
cash = Cash(25000)
cash.pay(5000)