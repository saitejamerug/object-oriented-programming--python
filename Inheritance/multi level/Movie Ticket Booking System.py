# Class 1: Movie
# • Create a method ticket(movie) that returns the ticket price.

# Class 2: Booking (inherits Movie)
# Create the following methods:
# • movies() – Display the available movies.
# • selection() – Allow the user to book multiple tickets.
# • billing() – Display the total amount and add a booking charge of ₹30.

# Class 3: Customer (inherits Booking)
# • Create an object and call the selection() method.

class Movie:
    def ticket(self, movie):
        movies = {
            "Bahubali": 250,
            "Ye jawani he diwani": 175,
            "Bajrangi": 220,
            "Maharshi": 350,
            "Interstellar": 500
        }
        return movies.get(movie)
class Booking(Movie):
    def movies(self):
        print("Bahubali: 250 \nYe jawani he diwani: 175 \nBajrangi: 220 \nMaharshi: 350 \nInterstellar: 500")
    def billing(self, cost):
        print("Your total movies value is :Rs.", cost)
        print("booking charge of ₹30")
        print("Total bill Rs.", cost + 30)
    def selection(self):
        total_amount = 0
        while True:
            self.movies()
            movie = input("Enter movie name:")
            total_amount += self.ticket(movie)
            choice = input("Want to book more tickets y/n?")
            if choice == "n":
                break
        self.billing(total_amount)

class Customer(Booking):
    pass
c1 = Customer()
c1.selection()