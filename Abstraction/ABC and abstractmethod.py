# Design an abstract class Payment Gateway (ABC) with abstract methods: initiate(amount),
# verify(transaction_id), and refund(transaction_id). Implement two concrete classes RazorpayGateway
# and PayPalGateway. Verify that you cannot instantiate PaymentGateway directly.

from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def initiate(self, amount):
        pass
    @abstractmethod
    def verify(self, transaction_id):
        pass
    @abstractmethod
    def refund(self, transaction_id):
        pass
class RazorPay(PaymentGateway):
    def initiate(self, amount):
        print(f"Initiating payment of Rs. {amount} via RazorPay.")
    def verify(self, transaction_id):
        print(f"Verifying transaction id : {transaction_id}.")
    def refund(self, transaction_id):
        print(f"Refund initiated for transaction id: {transaction_id}.")
class PayPal(PaymentGateway):
    def initiate(self, amount):
        print(f"Initiating payment of Rs. {amount} via PayPal")
    def verify(self, transaction_id):
        print(f"Verifying transaction id : {transaction_id}.")
    def refund(self, transaction_id):
        print(f"Refund initiated for transaction id: {transaction_id}")
obj = PaymentGateway()