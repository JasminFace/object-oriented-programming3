class Person:
    
    def __init__(self, name):
        self.name = name

    def greeting(self):
            print(f"Hi! name is {self.name}")


class Student(Person):

    def learn(self):
        print("I get it!")

class Instructor(Person):

    def teach(self):
        print("An object is an instance of class")


nadia = Instructor("Nadia")
chris = Student("Chris")

nadia.greeting()
chris.greeting()

nadia.teach()
chris.learn()

chris.teach()
# This doesn't work because Chris is part of the student class and the student class doesn't have teach. He can only learn ..for now.
