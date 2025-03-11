import datetime

class Bus:
    def __init__(self, bus_id, route, total_seats, departure_date, departure_time):
        self.bus_id = bus_id
        self.route = route
        self.total_seats = total_seats
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.available_seats = list(range(1, total_seats + 1))
        self.bookings = {}

    def book_ticket(self, passenger_name, seat_number):
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            self.bookings[seat_number] = passenger_name
            return (f"\n=================================================\n"
                    f"\033[92m  Ticket Confirmed!  \033[0m\n"
                    f"-------------------------------------------------\n"
                    f" Passenger: {passenger_name}\n"
                    f" Seat: {seat_number}\n"
                    f" Bus: {self.bus_id}\n"
                    f" Departure: {self.departure_date} at {self.departure_time}\n"
                    f"=================================================\n")
        return "\033[91m Seat not available! Choose another.\033[0m"

    def cancel_ticket(self, seat_number):
        if seat_number in self.bookings:
            passenger_name = self.bookings.pop(seat_number)
            self.available_seats.append(seat_number)
            self.available_seats.sort()
            return f"\033[91m Booking canceled for {passenger_name} - Seat {seat_number}\033[0m"
        return "\033[93m Seat not found!\033[0m"

    def display_seats(self):
        print("\n=================================================")
        print(f" Bus {self.bus_id} - {self.route} - Departure: {self.departure_date} {self.departure_time}")
        print("=================================================")
        for seat in range(1, self.total_seats + 1):
            if seat in self.bookings:
                print(f"\033[91m{seat:02}\033[0m", end=" ")
            else:
                print(f"\033[92m{seat:02}\033[0m", end=" ")
            if seat % 5 == 0:
                print()
        print("\n\033[92mAvailable (Green)\033[0m   \033[91mBooked (Red)\033[0m")
        print("=================================================")

# **User Interaction**
def main():
    routes = ["Phnom Penh -> Siem Reap", "Phnom Penh -> Battambang", "Phnom Penh -> Preah Sihanouk"]
    buses_per_route = 5
    total_seats = 45
    departure_times = [f"{hour}:00" for hour in range(7, 23)]
    
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
            print("\n=================================================")
            print(" Select a Route:")
            print("=================================================")
            for i, route in enumerate(routes, 1):
                print(f" {i}. {route}")
            print("=================================================")

            route_choice = int(input("Enter route number: ")) - 1
            if route_choice not in range(len(routes)):
                print("\033[93mInvalid route!\033[0m")
                continue
            
            selected_route = routes[route_choice]
            print(f"Selected Route: {selected_route}")
            
            print("\n=================================================")
            print(" Select a Bus:")
            print("=================================================")
            for i in range(1, buses_per_route + 1):
                print(f" {i}. Bus {100 + i}")
            print("=================================================")
            
            bus_choice = int(input("Enter bus number: "))
            if bus_choice not in range(1, buses_per_route + 1):
                print("\033[93mInvalid bus!\033[0m")
                continue
            
            selected_bus_id = 100 + bus_choice
            
            print("\n=================================================")
            print(" Select a Departure Date (YYYY-MM-DD):")
            print("=================================================")
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            while True:
                departure_date = input(f"Enter departure date ({current_date}-...): ")
                if departure_date >= current_date:
                    break
                print("\033[93mInvalid date! Please enter a future date.\033[0m")
            
            print("\n=================================================")
            print(" Select a Departure Time:")
            print("=================================================")
            for i, time in enumerate(departure_times, 1):
                print(f" {i}. {time}")
            print("=================================================")
            
            time_choice = int(input("Enter time number: ")) - 1
            if time_choice not in range(len(departure_times)):
                print("\033[93mInvalid time!\033[0m")
                continue
            
            selected_time = departure_times[time_choice]
            print(f"Selected Departure: {departure_date} {selected_time}")
            
            bus = Bus(bus_id=selected_bus_id, route=selected_route, total_seats=total_seats, departure_date=departure_date, departure_time=selected_time)
            
            # Now directly proceed to ticket booking
            bus.display_seats()
            name = input("Enter passenger name: ")
            seat = int(input("Enter seat number to book: "))
            print(bus.book_ticket(name, seat))
        
        elif choice == "2":
            print("Enter seat number to cancel: ")
            seat = int(input())
            bus.cancel_ticket(seat)

        elif choice == "3":
            bus.display_seats()
        
        elif choice == "4":
            print("Exiting... Have a safe journey!")
            break
        else:
            print("\033[93m Invalid choice! Try again.\033[0m")

# Run the booking system
if __name__ == "__main__":
    main()
