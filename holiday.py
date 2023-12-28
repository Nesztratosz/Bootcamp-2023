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

def hotel_cost(nights,place):  #function for the hotel cost

    if destination == "l":
        place = 56
    elif destination == "hk":
        place = 42
    elif destination == "la":
        place = 120
    elif destination == "b":
        place = 35
    elif destination == "m":
        place = 16

    hotel = nights * place
    return hotel

def plane_cost(plane):  #function for how much the plane cost
    if destination == "l":
        plane += 50
    elif destination == "hk":
        plane += 150
    elif destination == "la":
        plane += 76.8
    elif destination == "b":
        plane += 32
    elif destination == "m":
        plane += 16
    return plane

def car_rental(day,car):  # function for the car rental
    if destination == "l":
        car += 14
    elif destination == "hk":
        car += 12
    elif destination == "la":
        car += 7
    elif destination == "b":
        car += 3.2
    elif destination == "m":
        car += 2

    rental = car * day
    return rental


def holiday_cost(): # function for the sum total
    total = car_rental(day, 0) + hotel_cost(nights, 0) + plane_cost(0)
    return total




print("This program will calculate the holiday total cost.")
options()
destination = "x"

while destination != "q":
    destination = input("PLease give me the desired destination: ").lower()
    nights = int(input("Please give me how many night would you like to stay: "))
    day = int(input("Please give me how many days would you like to hire: "))
    #total = car_rental(day, 0) + hotel_cost(nights, 0) + plane_cost(0)
    if destination == "l":
        print(f"The hotel cost {hotel_cost(nights ,0)}£")
        print(f"The car rental is {car_rental(day ,0)}£")
        print(f"The flight is {plane_cost(0)}")
        print(f"The total holiday cost to London {holiday_cost()} £")
        options()

    elif destination == "hk":
        print(f"The hotel cost {hotel_cost(nights , 0)}£")
        print(f"The car rental is {car_rental(day , 0)}£")
        print(f"The flight is {plane_cost(0)}£")
        print(f"The total holiday cost to HongKong {holiday_cost()} £")
        options()

    elif destination == "la":
        print(f"The hotel cost {hotel_cost(nights ,0)}£")
        print(f"The car rental is {car_rental(day,0)}£")
        print(f"The flight is {plane_cost(0)}£")
        print(f"The total holiday cost to LosAngeles {holiday_cost()} £")
        options()

    elif destination == "b":
        print(f"The hotel cost {hotel_cost(nights,0)}£")
        print(f"The car rental is {car_rental(day,0)}£")
        print(f"The flight is {plane_cost(0)}£")
        print(f"The total holiday cost to Berlin {holiday_cost()} £")
        options()

    elif destination == "m":
        print(f"The hotel cost {hotel_cost(nights,0)}£")
        print(f"The car rental is {car_rental(day,0)}£")
        print(f"The flight is {plane_cost(0)}£")
        print(f"The total holiday cost to Madrid {holiday_cost()} £")
        options()

    elif destination == "q":
        print("Thank you for your enquiry Good Bye")

    else:
        print("Unrecognized option.")
        options()

