# tuples
print('tuples *****************************************')
empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
print(empty_tuple, one_el_tuple_a, one_el_tuple_b)
print('three element tuple')
three_element_tuple = 1,2,3
print(three_element_tuple)

# Mutability
print('Mutability *****************************************')
user_data = ('John', 'American', 1964)
print(user_data)
user_data = ('Katya', 'Russian', 1980)
print(user_data)
print(user_data[0])
#TypeError: tuple.count() takes exactly one argument (0 given)
#user_data[0] = 'Mark'
#Like string char assignment
#name = 'welcome'
#name[0] = 'W'

#Tuple operation
print('Tuple operation *****************************************')
user_data = ('John', 'American', 1964)
print(len(user_data))

user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This Person from the US!')

user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)

user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

numbers = (0,1) * 10
print(numbers)

# Tuple values can be a variable
first = 5
second = 7
first, second = second, first

# Tuples in lists,lists in tuples
print('Tuples in lists,lists in tuples *****************************************')
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
capitals = [city_1,city_2,city_3]
print(capitals)
for capital in capitals:
    print('Name:', capital[0],', Country:', capital[1],', Population:', capital[2])

# lists in a tuple
user_data = ('John', 'American', 1964, [77.00,78.2,77.5])
print(user_data)
user_data[3].append(79.6)
print(user_data)