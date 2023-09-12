# File predefined streams
# sys.stdin
# sys.stdout
# sys.stderr

import sys
from os import strerror

# for line in sys.stdin:
#    if line.rstrip() == 'q':
#        break
#    print(line)

sys.stdout.write('hello')
print()
# sys.stderr('This is error message')
print()
print('You processed q, so I want to quit now. Bye!')

# File diagnose errors

try:
    stream = open('nonexistent.text')
    stream.close()
except Exception as e:
    print('An error occurred: ', e)
    print(e.errno)
    print(strerror(e.errno))