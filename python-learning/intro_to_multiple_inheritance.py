class Vehicle():
    def go(self):
        print('Going!')

    def introduce(self):
        print('I am a Vehicle')

class Flyable():
    def fly(self):
        print('Flying!')

    def introduce(self):
        print('I am a Flyable')

class Airplane(Vehicle, Flyable):
    def introduce(self):
        print('I am an Airplane')

my_plane = Airplane()
my_plane.go()
my_plane.fly()

# MRO (Method Resolution Order)
# Python's MRO
# 1. Look inside the object.
# 2. If not found, look in the superclasses
#    from left to right
# 3. If not found, show an error.

my_plane.introduce()

print(Vehicle.__bases__)
print(Airplane.__bases__)
