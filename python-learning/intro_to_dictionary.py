# Intro to dictionary
# dictionary are collections use to store key value pairs
print('Intro to dictionary**********************************')
emails = {
    'Anne Stahl': 'astah1@gmail.com',
    'Peter Small': 'peters@gmail.com',
    'Mark Steel': 'mark@gmail.com'
}

print(emails)
print(emails['Anne Stahl'])

spanish_animals = {
    'dog': 'el perro',
    'cat': 'el goto',
    'horse': 'el caballo',
    'bird': 'el pajaro'
}

print(spanish_animals['bird'])

spanish_animals = {
    'dog': 'el perro',
    'cat': 'el goto',
    'horse': 'el caballo',
    'bird': 'el pajaro',
    'bird': 'el ave'
}

print(spanish_animals)

#Dictionay can have any imutable data types like int string tuple not list

# Dictionary Operation
print('Dictionary Operation **********************************')
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
grades['Anne'] = 'A'
print(grades)
grades.update({'John':'A'})
print(grades)
print(len(grades))
if 'John' in grades:
    print('John got:',grades['John'])
del grades['John']
print(grades)

# preyer to 3.6 Dictionary not ordered
# in 3.6 ordered collections by default
print('Dictionary iteration **********************************')
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
for el in grades:
    print(el)

for el in grades.keys():
    print(el)

for el in grades.values():
    print(el)

for person, grade in grades.items():
    print(person, 'got', grade)
