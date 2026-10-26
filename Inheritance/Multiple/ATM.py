# ATM System Using Multiple Inheritance
# Class 1: SBI
# • Create the methods deposit(amount) and check_balance().
# Class 2: UnionBank
# • Create the methods withdraw(amount) and mini_statement().
# Class 3: ATM (inherits SBI and UnionBank)
# • Create the methods menu() and transaction().
# • Allow the user to perform banking operations.
# Driver Code
# • Create an object of the ATM class.
# • Call the transaction() method.

class SBI:
    def __init__(self, balance):
        self.balance = balance
        self.statement = []

    def deposit(self, amount):
        self.balance += amount
        print("Deposited an amount Rs.", amount)
        
    def check_balance(self):
        balance = 0
        print("Current balance: ", balance)
        return balance

