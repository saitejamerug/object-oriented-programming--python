class Bank:
    bank_name = "ABC Bank"
    def __init__(self, acc_holder_name, accno, balance, pin):
        self.acc_holder_name = acc_holder_name
        self._accno = accno
        self.__balance = balance
        self.__pin = pin
    def get_balance(self):
        return self.__balance
    def set_balance(self, new_balance):
        self.__balance = new_balance
alice = Bank("alice", 1234567, 10000, 1234)
print(alice.acc_holder_name)
print(alice._accno)
print(alice.get_balance())
alice.set_balance(15000)
print(alice.get_balance())
#print(alice.__balance)
print(alice._Bank__balance)
