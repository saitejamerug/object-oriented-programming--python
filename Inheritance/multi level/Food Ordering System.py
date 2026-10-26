# 4. Food Ordering System Using Multilevel Inheritance
# Class 1: Restaurant
# • Create a method menu(item) that returns the price of the selected food item.

# Class 2: FoodCourt (inherits Restaurant)
# Create the following methods:
# • display_menu() – Display the available food items.
# • order() – Accept the food item from the user and allow multiple orders.
# • billing() – Display the total bill and add a packing charge of ₹20.

# Class 3: Customer (inherits FoodCourt)
# • Create an object of the Customer class.
# • Call the order() method.


class Restaurant:
    def menu(self, item):
        items = {
            'burger' : 150,
            'fries' : 70,
            'coke' : 40,
            'pizza' : 200
        }
        return items.get(item)
            # return items[item]
class FoodCourt(Restaurant):
    def display_menu(self):
        print("burger : Rs.150 \nfries : Rs.70 \ncoke : Rs.40 \n pizza : Rs.200")
    def billing(self, cost):
        print("Your total cart value is :Rs.", cost)
        print("Packaging Charges :Rs.", 20)
        print("Total Bill : Rs.", cost + 20)

    def order(self):
        total_cost = 0
        while True:
            self.display_menu()
            choice = input("Enter your order name:")
            total_cost += self.menu(choice)
            next = input("Do you want to continue with your order? y/n")
            if next == 'n':
                break
        self.billing(total_cost)
class Customer(FoodCourt):
    pass
c1 = Customer()
c1.order()