"""
First we define the functions
    is a menu
    count out of the hotel price for the given city
    flight to the given city
    car rental to the given city
    and a sum total for his/her holiday
Ask the customer for the location he/she desires
and give back how much would it cost for
hotel x amount days the flight and the car rental
with a loop check which destination he choose
and give back the appropriate values
"""
#Functions for the program
def options():  #Menu for the options
    print("Cities:")
    print("For London please type: L")
    print("For HongKong please type: HK")
    print("For Los Angeles please type: LA")
    print("For Berlin please type: B")
    print("For Madrid please type: M")
    print("To finish you enquiry and quit please type: Q")


def hotel_cost(place, days):
    return hotel_costs[place] * days


def plane_cost(destination):  #function for how much the plane cost
    if destination == "l":
        return 50
    elif destination == "hk":
        return 150
    elif destination == "la":
        return 76.8
    elif destination == "b":
        return 32
    elif destination == "m":
        return 16


def car_rental(days, place):  # function for the car rental
    return rental_costs[place] * days


def holiday_cost(car_days, hotel_days, place): # function for the sum total
    total = car_rental(car_days, place) + hotel_cost(place, hotel_days) + plane_cost(place)
    return total


def valid_int(prompt):
    while True:
        try:
            valid_input = int(input(prompt))
            return valid_input
        except ValueError:
            print("Invalid input")


print("This program will calculate the holiday total cost.")
options()
valid_choices = ["l", "hk", "la", "b", "m"]
hotel_costs = {"l": 400, "hk": 450, "la": 600, "b": 300, "m": 375}
rental_costs = {"l": 150, "hk": 125, "la": 100, "b": 115, "m": 175}



while True:
    destination = input("PLease give me the desired destination: ").lower()
    if destination not in valid_choices:
        print("Incorrect input")
        continue

    nights = valid_int("Enter number of nights: ")
    day = valid_int("Please give me how many days would you like to hire: ")
    print(f"The hotel cost {hotel_cost(destination ,nights)}£")
    print(f"The car rental is {car_rental(day ,destination)}£")
    print(f"The flight is {plane_cost(destination)}")
    print(f"The total holiday cost to London {holiday_cost(day, nights, destination)} £")
    break
