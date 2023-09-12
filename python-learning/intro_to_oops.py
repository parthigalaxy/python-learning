# OOPs
# in Object-oriented programing data and functions are kept together in objects
    # All Python constructors must have at least one parameter
# Data pieces inside objects are called: properties, attributes of fields
# also include functions inside objects are called methods

# procedural approach
def calculate_area(widht, height):
    return widht * height

width = 10 #int(input('What is the width? '))
height = 20 #int(input('What is the height? '))
area = calculate_area(width,height)
print('The area is', area)

age = 20 #int(input('What is the age? '))
strange_operation = calculate_area(age,height)
print('Your age multiplied by the height is', strange_operation)

# object approach
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

width = 10 #int(input('What is the width? '))
height = 20 #int(input('What is the height? '))
rectagle = Rectangle(width, height)
print('The area is ', rectagle.get_area())

# classes are templates use to create a objects
# instantiate object from classes
# mostly we used procedural programing in python
class User:
    def __init__(self):
        self.name = 'myName'

    def showName(self):
        print('My name is :', self.name)

my_name = User()
my_name.showName()