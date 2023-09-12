# Diamnond Problam

class Vehicle():
    def show_power_type(self):
        print('I can use power from various sources')

class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print('U can use power from electricity')

class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print('I can use poer from petrol')

class HybridCar(ElectricVehicle, PetrolVehicle):
    pass

my_hybrid_car = HybridCar()

# diamond problem solved using MRO
my_hybrid_car.show_power_type()
