# Login System
# Create an abstract class LoginSystem with:
#     login(username, password)
#     logout()
#     Create:
#         AdminLogin
#         UserLogin
#     Implement login differently for admin and normal users.

from abc import ABC, abstractmethod
class LoginSystem(ABC):
    @abstractmethod
    def login(self, username, password):
        pass
    @abstractmethod
    def logout(self):
        pass
class AdminLogin(LoginSystem):
    def login(self, username, password):
        if username == "sai" and password == 123456:
            print("Admin Logging in...")
        else:
            print("Invalid credentials!")
    def logout(self):
        print("Admin logging out...")
class UserLogin(LoginSystem):
    def login(self, username, password):
        if username == "sai" and password == 123456:
            print("User Logging in...")
        else:
            print("Login failed!")
    def logout(self):
        print("User logging out...")
adminlogin = AdminLogin()
adminlogin.login("sai", 123456)
adminlogin.logout()
print()
userlogin = UserLogin()
userlogin.login("sai", 123456)
userlogin.logout()