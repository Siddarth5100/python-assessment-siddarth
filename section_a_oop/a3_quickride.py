class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def calculate_fare(self, distance_km):
        pass

class Bike(Vehicle):
    def calculate_fare(self, distance_km):
        rate= 8 # per km
        base= 20
        total_cal = distance_km * rate
        return base + total_cal

class Auto(Vehicle):
    def calculate_fare(self, distance_km):
        rate= 12 # per km
        base= 30
        total_cal = distance_km * rate
        return base + total_cal

class Car(Vehicle):
    def calculate_fare(self, distance_km):
        rate= 18 # per km
        base= 50
        total_cal = distance_km * rate
        return base + total_cal
    

# v = Vehicle("TN-37 CW-5100")

# print(v.vehicle_number)
# v.calculate_fare(40)

# b = Bike("TN-37 CW-5100")

# print(b.vehicle_number)
# print(b.calculate_fare(40))

# c = Car("TN-37 CW-5100")
# print(c.calculate_fare(40))

# a = Auto("TN-37 CW-5100")
# print(a.calculate_fare(40))

