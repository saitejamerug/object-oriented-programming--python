# Computed Properties
# Create a class Circle with a private _ radius. Add @property radius (getter) and @radius.setter that
# validates the radius is positive. Add a computed @property area and @property circumference. Show that
# changing radius automatically updates both computed properties
import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("The radius is negative")
    @property
    def area(self):
        return 2 * math.pi * self.__radius * 2
    @property
    def circumference(self):
        return 2 * math.pi * self.__radius

circle1 = Circle(5)
print(circle1.radius)
print(circle1.area)
print(circle1.circumference)
print()
circle1 = Circle(6)
print(circle1.radius)
print(circle1.area)
print(circle1.circumference)
