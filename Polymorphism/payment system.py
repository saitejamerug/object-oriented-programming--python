# Polymorphism
# Build a payment system with a base class Payment(amount) and three subclasses:
# CreditCard, UPI, and NetBanking. Each overrides a method process() with its own logic.
# Write a function checkout(payment) that calls process() on any payment object and demonstrate
# polymorphism.

class Payment:
    def __init__(self, balance):
        self.balance = balance
    def process(self, amount):
        print("processing payment")

class CreditCard(Payment):
    def process(self, amount):
        print("processing payment of Rs.", amount, "via CreditCard")
        self.balance += amount
        print("Payment done using CreditCard")
        print("Total balance Rs.", self.balance)

class UPI(Payment):
    def process(self, amount):
        print("processing payment of Rs.", amount, "via UPI")
        self.balance += amount
        print("Payment done using UPI")
        print("Total balance Rs.",self.balance)

class NetBanking(Payment):
    def process(self, amount):
        print("processing payment of Rs.", amount, "via NetBanking")
        self.balance += amount
        print("Payment done using NetBanking")
        print("Total balance Rs.", self.balance)

def checkout(payment):
    payment.process(1500)

checkout(CreditCard(1000))
print()
checkout(UPI(1500))
print()
checkout(NetBanking(2000))