class Calculator:
    def __init__(self, num):
       self.number = num 
    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")

    def squareRoot(self):
        print(f"The value of {self.number} square Root is {self.number**0.5}")
    
    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")

    @staticmethod
    def gretting():
        print("** Welcome **")

a= Calculator(4)
a.gretting()
a.square()
a.squareRoot()
a.cube()