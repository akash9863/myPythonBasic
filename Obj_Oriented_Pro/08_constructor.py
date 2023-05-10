class Employee:
    company = "Google"
    
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
    
    def getDeatails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.subunit}")
    
    def getSalary(self, signature):
        print(f"{self.company} given Salary is {self.salary}\n{signature}")

    @staticmethod
    def great():
        print("Good Morning")
    @staticmethod
    def time():
        print("Time is 9am")

akash = Employee("Akash", 25000, "Engineer")
akash.getDeatails()