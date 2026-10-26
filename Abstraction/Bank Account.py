# Bank Account
# Create an abstract class BankAccount with two abstract methods:
#     deposit(amount)
#     withdraw(amount)
#     Creat:
#         SavingsAccount
#         CurrentAccount
#     Maintain the balance using an instance variable
from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited! \ncurrent balance:", self.balance)
        else:
            print("Enter Valid amount!")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(amount, "withdraw successful! \ncurrent balance", self.balance)

class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited! \ncurrent balance:", self.balance)
        else:
            print("Enter Valid amount!")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(amount, "withdraw successful! \ncurrent balance", self.balance)

savingsaccount = SavingsAccount(100000)
savingsaccount.deposit(20000)
savingsaccount.withdraw(50000)
print()
currentaccount = CurrentAccount(200000)
currentaccount.deposit(30000)
currentaccount.deposit(40000)
currentaccount.withdraw(80000)