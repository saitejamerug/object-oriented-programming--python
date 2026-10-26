# Class 1: Cab
# • Create methods to calculate the fare for Bike, Auto, and Car rides.

# Class 2: Uber (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 10% GST and apply a 15% discount if the bill is above ₹1000.

# Class 3: Ola (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 12% GST and apply a 20% discount if the bill is above ₹1500.

# Driver Code
# • Ask the user to choose Uber or Ola and call the booking() method.

class Cab:
    def fare(self, vehicle):
        vehicles = {
            "Bike": 50,
            "Car": 100,
            "Van": 150
        }
        return vehicles.get(vehicle)
class Uber(Cab):
    def menu(self):
        print()