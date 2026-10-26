from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
    @property
    def account_number(self):
        return self.__account_number
    @property
    def holder_name(self):
        return self.__holder_name
    @property
    def balance(self):
        return self.__balance
    @account_number.setter
    def account_number(self, number):
        self.__account_number = number
    @holder_name.setter
    def holder_name(self, name):
        self.__holder_name = name
    @balance.setter
    def balance(self, amount):
        self.__balance = amount
    @abstractmethod
    def calculate_interest(self):
        pass
    def display_details(self):
        print(self.__account_number)
        print(self.__holder_name)
        print(self.__balance)

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        rate = 0.04
        interest = self.balance * rate
        print(f"Savings Interest (4%): Rs.{interest:.2f}")
        return interest

    def display_details(self):
        print("\n--- Savings Account Details ---")
        super().display_details()
        print("Account Type: Savings")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        rate = 0.02
        interest = self.balance * rate
        print(f"Current Account Interest (2%): Rs.{interest:.2f}")
        return interest

    def display_details(self):
        print("\n--- Current Account Details ---")
        super().display_details()
        print("Account Type: Current")

s_account = SavingsAccount(12345678, 'Sai Teja Merugu', 250000)
print(s_account.balance)
print(s_account.account_number)
print(s_account.holder_name)
print(s_account.calculate_interest())
s_account.display_details()
