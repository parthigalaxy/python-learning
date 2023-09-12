# class Vehicle:
#     pass
#
# class LandVehicle(Vehicle):
#     pass
#
# class Car(LandVehicle):
#     pass
#
# print(issubclass(Car, LandVehicle))
# print(issubclass(LandVehicle, Vehicle))
# print(issubclass(Car, Vehicle))
# print(issubclass(Car, Car))

class Vehicle:
    class_message = 'This is a message from the Vehicle class'
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        #Vehicle.__init__(self, speed)
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(super().class_message)
        # print(Vehicle.class_message)

    def speed_up(self):
        self.speed += 5

class Car(LandVehicle):
    def super_speed(self):
        print('Super speed activated!')
        super().speed_up()
        super().speed_up()
        super().speed_up()

my_car = Car( 5, 10)
print(my_car.__dict__)
print(my_car.speed)
print(my_car.class_message)

my_car.super_speed()
print(my_car.speed)
my_car.speed_up()
print(my_car.__dict__)

# isinstance()

my_vehicle = Vehicle(50)
my_land_vechicle = LandVehicle(50, 4)
my_car = Car(60, 4)
print('*******************************')
print(isinstance(my_vehicle, Vehicle))
print(isinstance(my_land_vechicle, Vehicle))
print(isinstance(my_car, Vehicle))

print('*******************************')
print(isinstance(my_vehicle, LandVehicle))
print(isinstance(my_land_vechicle, LandVehicle))
print(isinstance(my_car, LandVehicle))

print('*******************************')
print(isinstance(my_vehicle, Car))
print(isinstance(my_land_vechicle, Car))
print(isinstance(my_car, Car))

print('*******************************')
my_vehicle = Vehicle(60)
my_new_vehicle = my_vehicle

print(my_vehicle is my_new_vehicle)

print('*******************************')

print(my_vehicle.__dict__, my_new_vehicle.__dict__)
my_vehicle.speed = 30
print(my_vehicle.__dict__, my_new_vehicle.__dict__)

print('*******************************')
my_vehicle = Vehicle(60)
my_new_vehicle = Vehicle(60)

print(my_vehicle.__dict__, my_new_vehicle.__dict__)
my_vehicle.speed = 30
print(my_vehicle.__dict__, my_new_vehicle.__dict__)

print('*******************************')

first_num = 5
second_num = 5
print(first_num is second_num)

first_num = 5
second_num = 2
second_num += 3
print(first_num is second_num)
print('*******************************')
first_str = 'hello'
second_str = 'hello'
print(first_str is second_str)

print('*******************************')
first_str = 'hello'
second_str = 'hell'
second_str += 'o'
print(first_str is second_str)
print(first_str == second_str)