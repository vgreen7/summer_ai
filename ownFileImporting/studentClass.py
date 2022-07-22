class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def myfunc(self):
        print("Hello my name is " + self.name + " my age is", self.age, "my grade is", self.grade)

p1 = Student("john", 17, 11)
#p1.myfunc()

class Course:
    def __init__(self, name, professor):
        self.name = name
        self.professor = professor

    def myfunc(self):
        print("Course name is: " + self.name)

c1 = Course("Biology", "Benedict")
#c1.myfunc()