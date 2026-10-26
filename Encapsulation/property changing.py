# Property Chaining
# Build a Person class using @property for first_name, last_name, and full_name. full_name should be a
# computed read-only property. Add a @full_name.setter that splits the input string on a space and updates
# first and last names separately.

class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
    @property
    def full_name(self):
        return self.__first_name + " " + self.__last_name
    @full_name.setter
    def full_name(self, full_name):
        self.__first_name, self.__last_name = full_name.split()
person = Person("Sai", "Merugu")
print(person.first_name)
print(person.last_name)
print(person.full_name)
print()
person.full_name = "Vishnu Rogers"
print(person.first_name)
print(person.last_name)
print(person.full_name)