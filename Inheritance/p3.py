class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_marks(self):
        return self.marks

class Result(Student):
    pass

obj = Result("Rajath", 100)
if obj.display_marks() > 50:
    print("Passed")
else:
    print("Failed")
