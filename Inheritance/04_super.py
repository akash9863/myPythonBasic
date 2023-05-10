class Person:
    country = "BD"
    def __init__(self):
        print("Initializing Person..\n")
    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initializing Employee..\n")
    def getSalary(self):
        print(f"Salary is {self.getSalary}")
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee and Breathing too")

class Programmer(Employee):
    company = "Fiverr"
    def __init__(self):
        super().__init__()
        print("Initializing Programmer..\n")
    def getSalary(self):
        print(f"No salary to programmer")
    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer and Breathing more")

#p = Person()
#p.takeBreath()

#e = Employee()
#e.takeBreath()

pr = Programmer()
#pr.takeBreath()
