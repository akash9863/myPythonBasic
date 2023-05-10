class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"{self.company} given Salary is {self.salary}\n{signature}")


akash = Employee()
akash.salary = 50000
akash.getSalary("Thanks")   # Employee.getSalary(akash)



