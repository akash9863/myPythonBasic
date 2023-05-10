class Employee:
    company = "SinCos"
    salary = 2500
    salaryBonus = 500
    #totalSalary = 3000

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

e= Employee()
print(e.totalSalary)
e.totalSalary = 2800
print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)
    