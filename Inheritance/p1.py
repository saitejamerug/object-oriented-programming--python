# emp_name  • salary • display_details()
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self. salary = salary

    def display_details(self):
        return f"Salary:{self.salary}"

    def bonus(self):
        self.salary += 2000
        return f"Total salary:{self.salary}"

class Manager(Employee):
    pass
emp = Manager("Sushanth", 70000)
print(emp.bonus())