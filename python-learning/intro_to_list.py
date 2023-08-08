#Collections in python
#lists
#tuples
#dictionaries

#lists
cites = []
cites = ['New York City','Los Angles', 'Chicago', 'Houston', 'Phoenix']

print(cites)
#Indexing is start 0
print(cites[0])
print(cites[1])

#IndexError: list index out of range
#print(cites[5])

# To get a last element from the end
print(cites[-1])
#Before Last element
print(cites[-2])

#Slicing to get a specific length of the list
print(cites[0:2])
print(cites[:2])
print(cites[3:])
print(cites[:])
print(cites)
print(cites[10:15])

print('Delete List ************************')
#Delete Lists
top_cities = ['New York City','Los Angles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[2]
print(top_cities)
print(top_cities[2])
del top_cities[3:]
print(top_cities)
del top_cities[:]
print(top_cities)
#Delete the variable
#del top_cities
#print(top_cities)

#Add new element in new list
print('Add new element in new list************************************')
book_ratings = [7,9,5,6,8]
book_ratings.append(4)
print(book_ratings)

book_ratings.insert(1,10)
print(book_ratings)

#Iterating lists
top_cities = ['New York City','Los Angles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current city:',city)

for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:',top_cities[city_index])

print('Sum up the integers from list******************')
#Sum up the integers from list
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)

# Changing the positions
# print('Changing the positions')
# first = input('Enter the first number:')
# second = input('Enter the second number:')
# print('Before swapping:', first, second)
# first, second = second, first
# print('After swapping:', first, second)

top_cities = ['New York City','Los Angles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

top_cities = ['New York City','Los Angles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

random_number = [2,5,0,-3,4]
random_number.sort()
print(random_number)
random_number.sort(reverse=True)
print(random_number)

# sorted
top_cities = ['New York City','Los Angles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)

#Checking element presence
print('Checking element presence**************************************************')
for char in 'happy message':
    print(char)

invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
# name = input('What is your name? ')
# # we can use not in also to check the list value
# if name in invited_guests:
#     print('Welcome!')
# else:
#     print('You are not invited!')

# Copying lists
print('Copying lists **************************************************')
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)

list_original = [1,2,3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

list_original = [1,2,3]
list_new = list_original[:]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

# List Comprehensions
print('List Comprehensions **************************************************')
numbers = [1,2,3,4]
numbers = []
for i in range(1,101):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(1,101)]
print(numbers)

numbers = [i for i in range(1,101) if i % 3 != 0]
print(numbers)

# Nested Lists
print('Nested Lists **************************************************')
countries = [1, 'UK', 2, 'US']
cells = [['A1','A2','A3'],['B1','B2','B3']]
print(cells[0])
print(cells[0][0])
print(cells[0][1])
print(cells[1][2])

cells = [['A1','A2','A3'],['B1','B2','B3']]
for x in cells:
    print('Element:', x)

cells = [['A1','A2','A3'],['B1','B2','B3']]
for x in cells:
    for y in x:
        print('Element:', y)
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

for row in table:
    for cell in row:
        print(cell, '', end=' ')
    print()

# Adding and multiplying lists
print('Adding and multiplying lists **************************************************')

list_us = ['New York City', 'Chicago']
list_uk = ['London', 'Bristol']
list_all = list_us + list_uk
print(list_all)

list_numbers = [0,1] * 10
print(list_numbers)

# Further String features
print('Further String features **************************************************')

fav_band = 'Green Day'
print(fav_band[6])
print(fav_band[:6])

# Not work
# fav_band[6] = 'M'

print(fav_band.upper())
print(fav_band.lower())

#isnumeric()
#isspace()