class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"Programmer name is {self.name}\nThe product is {self.product}")

akash = Programmer("Akash", "Skype")
siam = Programmer("Saim", "Azure") 
akash.getInfo()
siam.getInfo()