# Flight
# Dictionary to store all flights
flights = {}
def add_flight(flight_no, destination, available_seats, price):
    """
    Add a new flight with details
    """
    flights[flight_no] = {
        "destination": destination,
        "available_seats": available_seats,
        "price": price
    }
    print("Flight added successfully")
def book_ticket(flight_no):
    """
    Book a ticket if seats are available
    """
    if flight_no in flights:
        if flights[flight_no]["available_seats"] > 0:
            flights[flight_no]["available_seats"] -= 1
            print("Ticket booked successfully")
        else:
            print("No seats available, booking not allowed")
    else:
        print("Flight not found")
def cancel_ticket(flight_no):
    """
    Cancel ticket and increase available seats
    """
    if flight_no in flights:
        flights[flight_no]["available_seats"] += 1
        print("Ticket cancelled successfully")
    else:
        print("Flight not found")
def search_flight(destination):
    """
    Search flight by destination
    """
    for flight_no, details in flights.items():
        if details["destination"].lower() == destination.lower():
            print(flight_no, details)
def display_flights():
    """
    Display all flights with details
    """
    for flight_no, details in flights.items():
        print(flight_no, details)
# Call
add_flight("AI101", "London", 5, 500)
add_flight("AI102", "Paris", 2, 400)

display_flights()

book_ticket("AI101")
book_ticket("AI101")

display_flights()

search_flight("London")

cancel_ticket("AI101")

display_flights()

