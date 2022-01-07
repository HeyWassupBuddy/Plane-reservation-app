from random import choice
import time
from datetime import timedelta


countries = ['Ukraine', 'Russia', 'USA']
airports = {'Ukraine': ['Kiev Airport', 'Odessa Airport', 'Lviv Airport'],
            'Russia': ['Moskow Airport', 'St.Petersburg Airport', 'Vladivostok Airport'],
            'USA': ['New York Airport', 'Los Angeles Airport', 'San Francisco Airport']}

reservations = []
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'


def airflyReservation():
    print("How can i help you?p")
    res = input(' [1] Reserve new fly\n [2] Cancel reservaton\n [3] Get Actual Reservation keys\n [4] Exit\n')

    if res == '1':
        resNewFly()
    elif res == '2':
        delReservation()
    elif res == '3':
        get_actual_reservations()
    elif res == '4':
        quit()
    else:
        error_msg()


def resNewFly(reservation_code=''):
    print("Hi there, where are we going today?\n")

    for country in countries:
        print(country, end='\n')
    global start_country
    start_country = input('Choose your country: ')


    for airport in airports.get(start_country):
        print('-', airport)


    global start_airport
    start_airport = input("Choose your airport: ")
    for airport in airports.get(start_country):
        if start_airport in airport:
            for country in countries:
                print(country, end='\n')
            global destination_country
            destination_country = input('Choose your country: ')

            for airport in airports.get(destination_country):
                print('-', airport)
            global destination_airport
            destination_airport = input("Choose your airport: ")
            flycode()
    print(
        "Yours fly from {start_country} {start_airport} to {destination_country} {destination_airport} is booked. "
        "Have a good trip! \n Your reservation code is {res_code}".format(
            start_country=start_country, start_airport=start_airport, destination_country=destination_country,
            destination_airport=destination_airport, res_code=reservation_code))
    print(reservations)
    return start_country, start_airport, destination_country, destination_airport


def flycode(reservation_code=''):
    for i in range(4):
        reservation_code += choice(lowercase_letters)
        for res in reservations:
            if reservation_code == res:
                reservation_code += choice(lowercase_letters)

    reservations.append(reservation_code)
    remind = input('Should i remind you? [y/n]')
    if remind == 'y':
        reminder()
    else:
        pass


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
        print('from {start_country} {start_airport} to {destination_country} {destination_airport}'.format(start_country = start_country, start_airport = start_airport, destination_country = destination_country, destination_airport = destination_airport))
    if len(reservations) == 0:
        print('No actual reservations')

def reminder():
    text = "your trip to {}".format(destination_airport)
    print("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    print('Reminder created')
    time.sleep(local_time)
    print(text)

while True:
    airflyReservation()
