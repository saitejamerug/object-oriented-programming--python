# Create an Employee class with a private __salary. Use @property to get the salary and @salary.setter to modify it.
# Create an employee object and update the salary.

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
employee = Employee(1000)
print(employee.salary)
employee.salary = 2000
print(employee.salary)