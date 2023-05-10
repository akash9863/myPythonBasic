class Employee:
    company = "Visa"
    eCode = 120
class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLEvel(self):
        self.level= self.level + 1

class Programmer(Employee, Freelancer):
    name = "Akash"

p = Programmer()
p.upgradeLEvel()
print(p.level)
print(p.company)
