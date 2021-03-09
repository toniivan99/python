from random import randint
from Client import Client

print("Please enter you name:")
name = input()
client = Client(randint(1, 10000), name)

print("Please choose option:")
print("1. Get all cars")
print("2. Get only available cars")
print("3. Rent car(s) for hour(s)")
print("4. Rent car(s) for day")
print("5. Rent car(s) for week")
print("6. Exit")
option = int(input())

def printCars(cars):
    for car in cars:
        print("Brand: " + car.brand)
        print("Model: " + car.model)
        print("Consumption: " + str(car.consumption))
        print("License plate: " + car.licensePlate)
        print("Price per hour: " + str(car.pricePerHour))
        print("Price per day: " + str(car.pricePerDay))
        print("Price per week: " + str(car.pricePerWeek))
        print("Is car rented: " + str(car.isRented))
        if car.isRented:
            print("Client rented the car: " + str(car.rentedBy))
            print("Rented from date: " + car.rentedFrom.strftime('%Y-%m-%d %H:%M:%S.%f'))
            print("Rented to date: " + car.rentedTo.strftime('%Y-%m-%d %H:%M:%S.%f'))
        print("----------")

while option != 6:
    if option == 1:
        cars = client.getCarsCatalogFactory(False)
        printCars(cars)
        option = int(input())
    elif option == 2:
        cars = client.getCarsCatalogFactory(True)
        printCars(cars)
        option = int(input())
    elif option == 3:
        print("Please enter cars license plates separated by comma")
        licensePlates = input()
        print("Please enter hours")
        hours = int(input())
        sum = client.rentCarsForHours(licensePlates.split(','), hours)
        print("Total sum to pay: " + str(sum))
        option = int(input())
    elif option == 4:
        print("Please enter cars license plates separated by comma")
        licensePlates = input()
        sum = client.rentCarsForDay(licensePlates.split(','))
        print("Total sum to pay: " + str(sum))
        option = int(input())
    elif option == 5:
        print("Please enter cars license plates separated by comma")
        licensePlates = input()
        sum = client.rentCarsForWeek(licensePlates.split(','))
        print("Total sum to pay: " + str(sum))
        option = int(input())
    elif option == 6:
        break