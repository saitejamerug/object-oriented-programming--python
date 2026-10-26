# Create a Student class with a private variable __marks.Create methods: set_marks() to assign marks and get_marks() to retrieve marks.
# Create an object and access the marks using these methods.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks
s1 = Student(100)
print(s1.get_marks())
s1.set_marks(50)
print(s1.get_marks())