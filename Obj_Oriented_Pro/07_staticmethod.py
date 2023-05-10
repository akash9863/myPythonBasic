class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"{self.company} given Salary is {self.salary}\n{signature}")

    @staticmethod
    def great():
        print("Good Morning")
    @staticmethod
    def time():
        print("Time is 9am")

akash = Employee()
akash.time()
akash.great()     #Employee.great()
akash.salary = 50000
akash.getSalary("Thanks")   # Employee.getSalary(akash)



