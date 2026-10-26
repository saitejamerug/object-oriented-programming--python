# Create a BankAccount class with a private variable __balance.   Implement: deposit(amount), withdraw(amount), and get_balance().
# The balance should not be accessed directly from outside the class.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
s1 = BankAccount(10000)
print(s1.get_balance())