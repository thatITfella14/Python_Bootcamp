# List comprehension in Python provides a concise and efficient way to create new lists based on existing iterables (like lists, tuples, or strings). It offers a more compact and often more readable alternative to traditional for loops for list creation, filtering, and transformation.

# Example of creating list from a string without using list comprehension method.

mystring = "howdy"

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist) # output is ['h', 'o', 'w', 'd', 'y']

print()
print()

# using the list comprehensions method

# Example 1

string_a = "something"

list_a = [letter for letter in string_a]

print(list_a)

print()
print()


# Example 2

grades = [78, 92,52, 68, 70,83, 39, 46, 57, 73, 96]

passing_grades = [num for num in grades if num >= 70]

print(passing_grades)

print()
print()

# Example 3

list_b = [num**2 for num in range(0,11)]

print(list_b)

print()
print()

# Example 4 (list compreshension with "if" condition); in this example we want to create a list with even numbers from the range of 0,11

list_c = [num for num in range(0,11) if num % 2 == 0]

print(list_c)

print()
print()

# Example 5

celcius = [0,10,20,34.5,38]

fahrenheit = [((9/5) * temp + 32) for temp in celcius]

print(fahrenheit)

print()
print()

# Example 6 (if and else in list comprehension)

results = [x if x % 2 == 0 else "Odd" for x in range(0,11)]

print(results)

print()
print()

# Example 7 (nested loop  in list  comprehension)

list_d = []

for x in [1,2,3]:
    for y in [10,20,30]:
        list_d.append(x*y)

print(list_d)

print()
print()

# now below given is nested loop in list comprehension

list_d = [x * y for x in [1,2,3] for y in [10,20,30]]

print(list_d)

# take a good look at the one above the last one; one will find that one more readable and easily understandable, however the later one not so much if you were to come back to you code a few months later even though it's a sleek way to write a code. Remember, the readability of your code is much for important that writing a sleek line of code or even computational efficiency.