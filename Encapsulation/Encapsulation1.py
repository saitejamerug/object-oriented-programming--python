class Bank:
    Bank = "ABC Bank"
    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        accno = int(input("Enter accno: "))
        pin = int(input("Enter Pin: "))
        if accno == 1234567 and pin == 1234:
            return self.__balance
        else:
            return "Access Denied!!"
    @balance.setter
    def balance(self, new_balance):
        if new_balance > 0:
            self.__balance = new_balance
        else:
            print("Value cannot be zero!!")
sai = Bank(10000)
print(sai.balance)
sai.balance = 50000
