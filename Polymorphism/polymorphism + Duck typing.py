import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Hexagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

def total_area(shapes):
    area = 0
    for shape in shapes:
        area += shape.area()
    print(area)

shapes = [Circle(10), Rectangle(2, 4), Triangle(5, 6), Hexagon(10)]
total_area(shapes)