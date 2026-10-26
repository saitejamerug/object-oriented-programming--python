# Class 1: Course
# • Create a method fee(course) that returns the course fee.

# Class 2: Academy (inherits Course)
# Create the following methods:
# • courses() – Display available courses.
# • enroll() – Allow the user to enroll in multiple courses.
# • billing() – Display the total fee and add a registration fee of ₹100.

# Class 3: Student (inherits Academy)
# • Create an object and call the enroll() method.

class Course:
    def fee(self, course):
        courses = {
            "Python Fullstack": 37000,
            "Java Fullstack": 35000,
            "Data Science": 39000,
            "AIML": 45000
        }
        return courses.get(course)
class Academy(Course):
    def courses(self):
        print("Python Fullstack: 37000 \nJava Fullstack: 35000 \nData Science: 39000 \nAIML: 45000")

    def billing(self, total_cost):
        print("Your total fare Rs.", total_cost)
        print("registration fee of ₹100")
        print("Total course Rs.", total_cost + 100)

    def enroll(self):
        total_cost = 0
        while True:
            self.courses()
            course = input("Choose course:")
            choice = input("want to choose more courses y/n?")
            total_cost += self.fee(course)
            if choice == "n":
                break
        self.billing(total_cost)

class Student(Academy):
    pass
s1 = Student()
s1.enroll()