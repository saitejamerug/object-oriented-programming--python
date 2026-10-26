# @property + @setter
# Design a BankAccount class with a private balance. Create @property balance as a getter. Create a @balance.
# setter that raises ValueError if the value is negative. Add methods deposit(amount) and withdraw(amount)
# that update balance through the setter. Test all edge cases

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance):
        if balance > 0:
            self.__balance = balance
        else:
            raise ValueError
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount!!")
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds!!")
sai = BankAccount(10000)
print(sai.balance)
sai.balance = 50000
print(sai.balance)
sai.deposit(2000)
print(sai.balance)
sai.withdraw(25000)
print(sai.balance)