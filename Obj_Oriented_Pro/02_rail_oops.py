class RailForm:
    formType = "RailForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

myApplication = RailForm()
myApplication.name = "Akash"
myApplication.train = "Chottola"
myApplication.printData()
