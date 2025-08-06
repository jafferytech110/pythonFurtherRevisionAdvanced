class Car:
    #class variable
    countryOrigin = "United States"
    numOfCars = 0

    def __init__(self, model, year, color, forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale
        Car.numOfCars += 1

    def drive(self):
        print(f"{self.model} is being driven.")
    def stop(self):
        print("Car is not being driven.")


car2 = Car("Toyota", 2024, "Blue", True)
print(Car.countryOrigin)

car3 = Car("Honda", 2024, "Blue", True)
print(Car.numOfCars)