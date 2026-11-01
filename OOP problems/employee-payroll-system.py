from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, emp_id, salary):
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = salary
    @property
    def name(self):
        return self.__name
    @property
    def emp_id(self):
        return self.__emp_id
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, n_salary):
        if n_salary < 0:
            raise ValueError('Salary cannot be in negative')
        self.__salary = n_salary
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_details(self):
        print(f"Name: {self.__name}, id: {self.__emp_id}, salary: {self.calculate_salary()}")

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary, bonus):
        super().__init__(name, emp_id, salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.salary + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours, hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate
        super().__init__(name, emp_id, 0.0)
    def calculate_salary(self):
        return self.hours * self.hourly_rate

class ContractEmployee(Employee):
    def __init__(self, name, emp_id, contract_amount):
        super().__init__(name, emp_id, contract_amount)
    def calculate_salary(self):
        return self.salary

fte = FullTimeEmployee("Sai Teja Merugu", 873498, 40000, 5000.0)
pte = PartTimeEmployee("Pavan", 984512, 40, 500.0)
ce = ContractEmployee('Nikith kumar', 762390, 35000.0)

for obj in [fte, pte, ce]:
    obj.display_details()

print(pte.calculate_salary())
print(fte.salary)
print(pte.name)
print(ce.emp_id)
fte.salary = 50000
print(fte.salary)