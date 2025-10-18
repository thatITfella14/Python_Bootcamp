# Functions are reusable blocks of code that perform a specific task. They help to organize code, make it more readable, and allow for code reuse.

# Creating a function requires a very specific syntax, including the def keyword, correct identation, and proper structure.

# Example 1
def say_hello():
    print("Hello!")

say_hello()  # Calling the function to execute its code

print()

# Example 2

def say_name(name):
    print(f"Hello, {name}!")

say_name("Kira")

print()

# Difference between print and return:

# The core difference between print and return in Python is their purpose: print is for displaying output to a user, while return is for sending a value from a function back to the code that called it.

def add_num(num1,num2):
    return num1 + num2

result = add_num(10,20)

print(result) # output: 30

print()

# Another example:

result = add_num(5,7)

print(result) # Output: 12

print()

# You can pass the print and return under the same function. It's not very common, but it can be done. Imagine a situation where you want to log the result of a calculation for debugging purposes, but also want to return the result for further use.

def multiply_num(a,b):
    print(a * b)  # this will print
    return a * b

result1 = multiply_num(2,2) # this will store the return value in result1 and print the value as well when print is called upon it down below

print(result1)