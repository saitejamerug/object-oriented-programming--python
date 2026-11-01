from abc import ABC, abstractmethod
class FoodOrder(ABC):
    # initializing values
    def __init__(self, order_id, customer_name, amount):
        self.__order_id = order_id
        self.__customer_name = customer_name
        self.__amount = amount

    # property getter for accessing private attributes
    @property
    def order_id(self):
        return self.__order_id
    @property
    def customer_name(self):
        return self.__customer_name
    @property
    def amount(self):
        return self.__amount

    # setter for modifying private attributes
    @order_id.setter
    def order_id(self, new_id):
        self.__order_id = new_id
    @customer_name.setter
    def customer_name(self, new_name):
        self.__customer_name = new_name
    @amount.setter
    def amount(self, new_amount):
        if self.__amount < 0:
            raise
        self.__amount = new_amount

    @abstractmethod
    def calculate_delivery_charge(self):
        pass

class SwiggyOrder(FoodOrder):
    def calculate_delivery_charge(self):
        return 0 if self.amount >=500 else 40

class ZomatoOrder(FoodOrder):
    def calculate_delivery_charge(self):
        return max(30, self.amount * 0.10)

class RestaurantOrder(FoodOrder):
    def calculate_delivery_charge(self):
        return 45

orders = [
    ZomatoOrder(78235, 'venkat', 799),
    SwiggyOrder(567, 'seenu', 999),
    RestaurantOrder(56, 'sai teja', 1249)
]

for order in orders:
    print(order.calculate_delivery_charge())