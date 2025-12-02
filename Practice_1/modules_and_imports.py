# Q 1: Import the math module and print the square root of 225.

from pathlib import PureWindowsPath
import math

number = 225

result = math.sqrt(number)

print(result)

print()

# Q 2: Use the random module to print a random integer between 1 and 6 (inclusive).

from random import randint

print(randint(1,6))

print()

# Q 3:  Import only the choice function from the random module and use it to pick a random item from ['red', 'green', 'blue'].

from random import choice

colors = ['red', 'green', 'blue']

print(choice(colors))

print()

# Q 4: Print today's date using the datetime module (you can hardcode '2025-12-01').

from datetime import date

print(date.today())

print()

#Q 5: Import the os module and print the current working directory.

import os

working_dir = os.getcwd()

print(working_dir)

print()