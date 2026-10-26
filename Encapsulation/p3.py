# Create a User class with a private variable: __password.   Create a method change_password() that allows the user to change the
# password.   The password should not be directly accessible from outside the class.

class User:
    def __init__(self, password):
        self.__password = password

    def change_password(self, password):
        self.__password = password
u1 = User("Sai123")
u1.change_password("Vishnu143")
