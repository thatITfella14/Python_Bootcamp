# Q 1: Write a function add_five(x) that takes a number and returns it plus 5. Test with x = 12.

def add_five(x):
    return x + 5

print(add_five(12))

print()
print()

# Q 2: Define a function is_even(n) that returns True if n is even, and False otherwise. Test with n = 17 and n = 24.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(is_even(17))

print(is_even(24))

print()
print()

# Q 3: Write a function first_last(lst) that returns a tuple with the first and last elements of a list. Test with [11, 22, 33, 44, 55].

list = [11, 22, 33, 44, 55]

def first_last(lst):
    return lst[0], lst[-1]

my_tuple = tuple(first_last(list))

print(my_tuple)

print()
print()

# Q 4: Write a function that takes two strings and returns True if they are anagrams. Test with 'apple' and 'papel'.

str1 = 'apple'

str2 = "papel"

def str_check(str1,str2):
    return sorted(str1) == sorted(str2)

print(str_check(str1,str2))

print()
print()

# Q 5: Define a function that takes a string and returns it in uppercase with exclamation marks on both ends. Test with 'hello'.

string = "hello"

def all_caps(string):
    return string.upper()

print("!"+all_caps(string)+"!")