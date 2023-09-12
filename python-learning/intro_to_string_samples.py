# String methods

print('isalnum() -> ', 'Adrian'.isalnum())
print('isalpha() -> ', 'Adrian'.isalpha())
print('isdigit() -> ', 'Adrian'.isdigit())
print('islower() -> ', 'Adrian'.islower())
print('isupper() -> ', 'Adrian'.isupper())
print('isspace() -> ', 'Adrian'.isspace())

# Joining, splitting and sorting strings
# Space should be there to start Join
print(' '.join(['This is', 'a spectacular','place to be']))

# Split
print('How many\tstrins\nwill you see?'.split())

# Sorting
# sorted returns a copy of the sorted elements
names = ['Adam', 'Kate', 'Barbara', 'Donna']
names_sorted = sorted(names)
print(names)
print(names_sorted)

# sort is changes the orignla list
names.sort()
print(names)

# String Comparisons

print('Python' == 'Python')
print('Python' == 'python')
print('Python' != 'Python')
print('Python' == 'Pytho')

print('Python' >= 'python')
print('Python' <= 'python')
print('Python' >= 'pytho')
print('Python' >= 'z')

# Compare first element values
print('20' >= '8')

# We could compare == or != with string and number orther compartion result in error
print(10 != 10)
print(10 == '10')

print(ord('d') - ord('a'))
# print(float('1,3'))