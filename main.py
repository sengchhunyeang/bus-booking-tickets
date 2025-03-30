import datetime

# Define color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class Bus:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = list(range(1, total_seats + 1))
        self.bookings = {}

    def book_ticket(self, passenger_name, seat_number):
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            self.bookings[seat_number] = passenger_name
            return (f"\n=================================================\n"
                    f"{GREEN}  Ticket Confirmed!  {RESET}\n"
                    f"-------------------------------------------------\n"
                    f" Passenger: {passenger_name}\n"
                    f" Seat: {seat_number}\n"
                    f"=================================================\n")
        return f"{RED} Seat not available! Choose another.{RESET}"

    def cancel_ticket(self, seat_number):
        if seat_number in self.bookings:
            passenger_name = self.bookings.pop(seat_number)
            self.available_seats.append(seat_number)
            self.available_seats.sort()
            return f"{RED} Booking canceled for {passenger_name} - Seat {seat_number}{RESET}"
        return f"{YELLOW} Seat not found!{RESET}"

    def display_seats(self):
        print("\n=================================================")
        print(" Bus - Available Seats")
        print("=================================================")
        for seat in range(1, self.total_seats + 1):
            if seat in self.bookings:
                print(f"{RED}{seat:02}{RESET}", end=" ")
            else:
                print(f"{GREEN}{seat:02}{RESET}", end=" ")
            if seat % 5 == 0:
                print()
        print(f"\n{GREEN}Available (Green){RESET}   {RED}Booked (Red){RESET}")
        print("=================================================")

# **User Interaction**
def main():
    total_seats = 45
    bus = Bus(total_seats)
    
    while True:
        print("\n=================================================")
        print(" Bus Booking System")
        print("=================================================")
        print(" 1. Book a Ticket")
        print(" 2. Cancel a Ticket")
        print(" 3. Show Available Seats")
        print(" 4. Exit")
        print("=================================================")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            bus.display_seats()
            name = input("Enter passenger name: ")
            seat = int(input("Enter seat number to book: "))
            print(bus.book_ticket(name, seat))
        
        elif choice == "2":
            seat = int(input("Enter seat number to cancel: "))
            print(bus.cancel_ticket(seat))

        elif choice == "3":
            bus.display_seats()
        
        elif choice == "4":
            print("Exiting... Have a safe journey!")
            break
        else:
            print(f"{YELLOW} Invalid choice! Try again.{RESET}")

# Run the booking system
if __name__ == "__main__":
    main()
