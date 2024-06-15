class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self, horse):
        self.horse = horse
        print(f'{self.horse} лошадиных сил')

class Nissan(Vehicle, Car):
    def __init__(self):
        self.vehicle_type = "No"
        self.price = 2000000
    def horse_powers(self, horses):
        self.horse = horses
        print(f'{self.horse} сил лошадиных')

vehicle_ = Vehicle()
car_ = Car()
nissan_ = Nissan()

print(vehicle_.vehicle_type)
print(car_.price)
car_.horse_powers(50)

print(nissan_.vehicle_type, nissan_.price)
nissan_.horse_powers(75)
