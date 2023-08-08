# Intro to function
print('Intro to function ************************')

def greet():
    print('Hello, World!')

greet()

# Function with Parameters
input_number = [5.0,3.5,7.8,9.9,10.0]

def get_average(input_mubers):
    sum =0.0;
    for number in  input_number:
        sum += number
    average = sum / len(input_number)
    print(average)

get_average(input_number)

# Mote then one Param
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count('Welcome', 'e')
print_letter_count('People say nothing is impossible, but I do nothing every day', 'a')

# Default param Values
print('Default param Values ************************')
print('Hello', 'How are you?', end='.',sep='-')

def print_letter_count(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count('How many letters a are here?')

# Key word arg must apper on the end
# all positional arguments must appear before any named arguments

# name scopes Shadowing
def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

# Access global variable use the global keyword in front of the variable
# like global mysterious_var
def show_truth_global():
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
print(mysterious_var)
show_truth_global()
print(mysterious_var)

def show_truth_list():
    mysterious_vars.append('New Surprise!')
    print(mysterious_vars)
    del mysterious_vars[0]

print('list scopes ********************')
mysterious_vars = ['Surprise!']
print(mysterious_vars)
show_truth_list()
print(mysterious_vars)

# None value
# Function can tyoically
# Cause some effect and return a meaningful value
print('hello')
length = len('hello')
print(length)
print(print('Test'))

x = None

if x is True:
    print('None is True')
elif x is False:
    print('None is False')
else:
    print('None is not True, of False, None is just None')

x = None
if x is None:
    print('Yes')
if x == None:
    print('if dose')

def greet():
    print('hello')
x = greet()
print(x)

# The return keyword
print('The return keyword *****************************************')
def get_average(input_mubers):
    sum =0.0;
    for number in  input_number:
        sum += number
    average = sum / len(input_number)
    return average

input_number = [5.0,3.5,7.8,9.9,10.0]
print(get_average(input_number))
average = get_average(input_number)
if average > 5:
    print('The average is too high!')

def is_frist_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
print(is_frist_last_equal([10,20,30,40,10]))
print(is_frist_last_equal([10,20,30,40,50]))
print(is_frist_last_equal([]))

# Recursion
print('Recursion *************************************************************')
# factorial
# 3! = 1 * 2 * 3 = 6
# 5% = 1 * 2 * 3 * 4 * 5 = 120

def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return  factorial

print(get_factorial(6))

