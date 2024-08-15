# Task 1

flight_interary = (["Alice", "New York", "London"],["Bob", "Tokyo", "San Francisco"])

def add_customer():
    
    name = input("\nWhat is your name\n")

    origin = input("\nWhere are you coming from?\n")

    destination = input("\nWhere are you wanting to go?\n")
    
    new_flight = [[name, origin, destination]]
    new_flight_list = list(new_flight)
    new_flight_tuple = tuple(new_flight_list)
    global newest_flight_interary
    newest_flight_interary = flight_interary + new_flight_tuple 
    print(newest_flight_interary)
    
def list_customers():
    global newest_flight_interary
    for i, (name, origin, destination) in enumerate(newest_flight_interary, start=1):
        print(f"Itinerary {i}: {name} - From {origin} to {destination}\n")


while True:
    print("\nFlight Itneraries Menu:")
    print("1. Add another customer")
    print("2. Look at list of customers")
    print("3. Quit the Program")

    try:
        decision = input('\nWhat would you like to do?\n')
    except ValueError:
        print("Please enter a number.")


    if decision == "1": # Add Customer
        add_customer()
    elif decision == "2": # List of Customers
        list_customers()
    elif decision == "3": # Quit Program
        break
    else:
        print("Invalid input. Please enter a number and try again.\n")


