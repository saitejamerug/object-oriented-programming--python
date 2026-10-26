# Authentication is the process of verifying who you are,
# authorization is the process of verifying what you have access to
# Explain in your own words: what is the difference between abstraction and encapsulation?
# Write one class example that demonstrates BOTH concepts at the same time

from abc import ABC, abstractmethod
class Bank(ABC):
     @property
     @abstractmethod
     def balance(self): #get_balance
         pass
     @abstractmethod
     def deposit(self, amount): # deposit money
         pass
     @abstractmethod
     def withdraw(self, amount):    # withdraw money
         pass
     @balance.setter
     @abstractmethod
     def balance(self, amount): # set balance
         pass
class Payment(Bank):
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance
    @balance.setter             # use getter variable name for setter
    def balance(self, balance):
        self.__balance = balance


payment = Payment(25000)
payment.balance = 20000
payment.deposit(5000)
print(payment.balance)

# we can set only if we make getter