class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"Train Name: {self.name}")
        print(f"Seats Available: {self.seats}")

    def get_fare(self):
        print(f"Ticket Fare: Rs {self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, this train is full! No seats available.")


# Creating a train object
intercity = Train("Intercity Express (14015)", 90, 2)

# Checking status and fare
intercity.get_status()
intercity.get_fare()

# Booking tickets
print("\n--- Booking 1st Ticket ---")
intercity.book_ticket()

print("\n--- Booking 2nd Ticket ---")
intercity.book_ticket()

print("\n--- Trying to Book 3rd Ticket ---")
intercity.book_ticket()

# Checking status again after bookings
print("\n--- Updated Status ---")
intercity.get_status()

