import json
from datetime import datetime

from Car import Car

class RentCarSystem:
    allCars = []

    @staticmethod
    def calculateSum(cars, fromDate, toDate):
        totalSum = 0
        for i in range(len(cars)):
            weeks = (toDate - fromDate).days // 7
            days = (toDate - fromDate).days
            hours = (toDate - fromDate).total_seconds() / 3600

            if weeks > 0:
                totalSum += weeks * cars[i].pricePerWeek
                days -= (weeks * 7)
                hours -= (weeks * 7) * 24

            if days > 0:
                totalSum += days * cars[i].pricePerDay
                hours -= days * 24

            if hours > 0:
                totalSum += (hours * cars[i].pricePerHour)

        if len(cars) > 3:
            return totalSum - (totalSum * 0.3)
        else:
            return totalSum

    @staticmethod
    def getAvailableCars():
        cars = RentCarSystem.getAllCars()
        availableCars = []
        for car in cars:
            if not car.isRented:
                availableCars.append(car)

        return availableCars

    @staticmethod
    def getAllCars():
        if len(RentCarSystem.allCars) > 0:
            return RentCarSystem.allCars.copy()
        else:
            file = open('cars.json')
            fileData = json.load(file)
            for data in fileData:
                brand = data['brand']
                model = data['model']
                consumption = data['consumption']
                licensePlate = data['licensePlate']
                pricePerHour = data['pricePerHour']
                pricePerDay = data['pricePerDay']
                pricePerWeek = data['pricePerWeek']
                isRented = data['isRented']
                if isRented:
                    rentedBy = data['rentedBy']
                    rentedFrom = datetime.strptime(data['rentedFrom'], '%Y-%m-%d %H:%M:%S.%f')
                    rentedTo = datetime.strptime(data['rentedTo'], '%Y-%m-%d %H:%M:%S.%f')
                else:
                    rentedBy = ""
                    rentedFrom = ""
                    rentedTo = ""
                car = Car(brand, model, consumption, licensePlate, pricePerHour, pricePerDay, pricePerWeek, isRented, rentedBy,
                          rentedFrom, rentedTo)
                RentCarSystem.allCars.append(car)

            file.close()
            return RentCarSystem.allCars.copy()

    @staticmethod
    def rentCars(cars, fromDate, toDate, clientId):
        for car in cars:
            if car.isRented:
                if car.rentedTo >= fromDate:
                    print("Car with license plate " + car.licensePlate + " is already rented")
                    return

        for car in cars:
            car.isRented = True
            car.rentedFrom = fromDate
            car.rentedTo = toDate
            car.rentedBy = clientId

        RentCarSystem.saveAllCars()
        return RentCarSystem.calculateSum(cars, fromDate, toDate)

    @staticmethod
    def saveAllCars():
        for car in RentCarSystem.allCars:
            if car.isRented:
                car.rentedFrom = car.rentedFrom.strftime('%Y-%m-%d %H:%M:%S.%f')
                car.rentedTo = car.rentedTo.strftime('%Y-%m-%d %H:%M:%S.%f')

        jsonFile = open('cars.json', "w")
        json.dump(RentCarSystem.allCars, jsonFile, indent=4, default=lambda x: x.__dict__)