class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"Train Name = {self.name}\nAvalable seat = {self.seats}")

    def fareInfo(self):
        print(f"Fare is {self.fare} Taka")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Ticket has been booked\nSeat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry! No seats are available")

  #  def cancelTicket(self):  
  
intercity = Train("Chottola",50, 2 )
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()

intercity.getStatus()
intercity.bookTicket()

intercity.getStatus()
intercity.bookTicket()

