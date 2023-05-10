class Employee:
    company = "Camel"
    salary = 100
    location = "Dhaka"

    #def changeSalary(self, sal):
        #self.salary = sal
        #self.__class__.salary = sal   #dunder
    @classmethod
    def changeSalary(cls, salary):    #changeClassAttribute
        cls.salary = salary

e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)