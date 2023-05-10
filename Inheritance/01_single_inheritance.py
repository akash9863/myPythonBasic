class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "YouTube"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("This is a Programmer")

e= Employee()
e.showDetails()
print(e.company)
p= Programmer()
p.showDetails()
print(p.company)
