class Person:
    country = "BD"
    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary is {self.getSalary}")
    def takeBreath(self):
        print("I am an Employee and Breathing too")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print(f"No salary to programmer")
    def takeBreath(self):
        print("I am a Programmer and Breathing more")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
