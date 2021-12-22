from random import choice

countries = ['Ukraine', 'Russia', 'USA', 'Belarus']
airports = {'Ukraine':['Kiev Airport', 'Odessa Airport', 'Lvov Airport'], 'Russia':['Moskow Airport','St.Petersburg Airport', 'Vladivostok Airport'], 'USA':['New York Airport', 'Los Angeles Airport', 'San Francisco Airport']}


reservations = []
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'



def airflyReservation():
    print("How can i help you?p")
    res = input(' [a] Reserve new fly\n [b] Cancel reservaton\n [c]Get Actual Reservation keys\n [d] Exit\n')

    if res == 'a':
        resNewFly()
    elif res == 'b':
        delReservation()
    elif res == 'c':
        get_actual_reservations()
    elif res == 'd':
        quit()
    else:
        error_msg()


def resNewFly(reservation_code=''):
    print("Hi there, where are we going today?\n")

    for country in countries:
        print(country, end='\n')
    start_country = input('Choose your country: ')

    for airport in airports.get(start_country):
        print('-', airport)

    start_airport = input("Choose your airport: ")
    for airport in airports.get(start_country):
        if start_airport in airport:
            for country in countries:
                print(country, end='\n')
            destination_country = input('Choose your country: ')
            for airport in airports.get(destination_country):
                print('-', airport)
            destination_airport = input("Choose your airport: ")
            flycode()
    print(
        "Yours fly from {start_country} {start_airport} to {destination_country} {destination_airport} is booked. Have a good trip! \n Your reservation code is {res_code}".format(
            start_country=start_country, start_airport = start_airport, destination_country=destination_country,destination_airport = destination_airport, res_code=reservation_code))
    print(reservations)

def flycode(reservation_code=''):
    for i in range(4):
        reservation_code += choice(lowercase_letters)
        for res in reservations:
            if reservation_code == res:
                reservation_code += choice(lowercase_letters)

    reservations.append(reservation_code)

def delReservation():
    request = input("If you want to delete reservation - please enter your reservation code: ")
    if request in reservations:
        reservations.remove(request)
        print('Reservation deleted')
    else:
        print('Invalid reservation code')

def error_msg():
    print('Error. Try again!')
def get_actual_reservations():
    for res in reservations:
        print('-',res)

while True:
    airflyReservation()
