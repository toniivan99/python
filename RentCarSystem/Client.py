from datetime import datetime, timedelta

from RentCarSystem import RentCarSystem

class Client:
    def __init__(self, clientId, name):
        self.clientId = clientId
        self.name = name

    def getCarsCatalogFactory(self, onlyAvailableCars):
        if onlyAvailableCars:
            return RentCarSystem.getAvailableCars()
        else:
            return RentCarSystem.getAllCars()

    def rentCarsForHours(self, licensePlates, hours):
        fromDate = datetime.now()
        toDate = fromDate + timedelta(hours=hours)

        cars = self.getCarsCatalogFactory(False)
        carsToRent = []
        for car in cars:
            if car.licensePlate in licensePlates:
                carsToRent.append(car)

        return RentCarSystem.rentCars(carsToRent, fromDate, toDate, self.clientId)

    def rentCarsForDay(self, licensePlates):
        fromDate = datetime.now()
        toDate = fromDate + timedelta(days=1)

        cars = self.getCarsCatalogFactory(False)
        carsToRent = []
        for car in cars:
            if car.licensePlate in licensePlates:
                carsToRent.append(car)

        return RentCarSystem.rentCars(carsToRent, fromDate, toDate, self.clientId)

    def rentCarsForWeek(self, licensePlates):
        fromDate = datetime.now()
        toDate = fromDate + timedelta(days=7)

        cars = self.getCarsCatalogFactory(False)
        carsToRent = []
        for car in cars:
            if car.licensePlate in licensePlates:
                carsToRent.append(car)

        return RentCarSystem.rentCars(carsToRent, fromDate, toDate, self.clientId)