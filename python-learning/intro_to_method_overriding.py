class Animal():
    def __init__(self):
        self.species = 'general'

    def produce_sound(self):
        print('General animal sound')

    def present(self):
        print('I can do the following sound:')
        self.produce_sound()

class Dog(Animal):
    def __init__(self):
        self.species = 'Canis familiaris'

# Method overriding
# polymorphism is the ablity of classes to take different forms
    def produce_sound(self):
        print('woof', 'woof!')

my_pet = Dog()
print(my_pet.species)
my_pet.produce_sound()

my_first_pet = Animal()
my_second_pet = Dog()

my_first_pet.produce_sound()
my_second_pet.produce_sound()

my_first_pet.present()
my_second_pet.present()
