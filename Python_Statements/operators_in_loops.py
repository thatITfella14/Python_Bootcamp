# the range() function is used to generate a sequence of numbers. It is commonly used in for loops for iteration. The range() function is not an "operator" in the same sense as arithmetic operators (like + or -) but rather a built-in function that creates a special "range object."

# range(stop): Generates numbers from 0 up to (but not including) stop, with a step of 1.

# range(start, stop): Generates numbers from start up to (but not including) stop, with a step of 1.

# range(start, stop, step): Generates numbers from start up to (but not including) stop, with an increment (or decrement) of step.

# Example 1; range()

for num in range(10):
    print(num)

print()
print()

for num in range(4,10):
    print(num)

print()
print()

for num in range(0,10,2):
    print(num)

print()
print()

# Example 2; cast a range() to a list

print(range(0,10,2)) # this will just output the range operator; however to cast it to a list do as follows

print()
print()

print(list(range(0,10)))

print()

print(list(range(0,10,2)))

print()
print()

# enumerate() function; The enumerate() function in Python is a built-in function that adds a counter to an iterable object, returning an enumerate object. This object can then be iterated over, yielding pairs of (index, value) for each item in the original iterable.

# below is the example of iteration without using the enumerate() function

index_count = 0

for letter in "abcdef":
    print("At index {} the letter is {}".format(index_count,letter))
    index_count = index_count + 1

print()
print()

# now the same output but using the enumerate() function

word = "abcdef"

for letter in enumerate(word):
    print(letter) # this will output in tuples format (0, 'a'), (1, 'b').......etc

print()
print()

# we can do tuple unpacking as follows

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

print()
print()

# zip() function; The zip() function in Python is a built-in function used to combine elements from multiple iterables (such as lists, tuples, or strings) into a single iterable of tuples. Each tuple contains elements from the corresponding position of the input iterables.

mylist1 = [1,2,3,4,5,6]
mylist2 = ["a","b","c","d","e","f"]

for letter in zip(mylist1,mylist2):
    print(letter)

print()
print()

# "in" operator; The in operator in Python is a membership operator used to check for the presence of a value within a sequence or collection. It returns a boolean value: True if the value is found, and False otherwise.

print('a' in [1,2,3]) # False

print()

print(2 in (1,2,3)) # True

print()

d = {"key1" : "test",
     "key2": 144}

print("key3" in d) # False

print()

print("key1" in d.values()) # False becayse key1 is a key, not a value

print()

print(144 in d.values()) # True because 144 is one the values in the dictonary named "d"

print()
print()

# min() & max() function

list_a = [10,20,30,40,50,60,70,80,90,100]

print(min(list_a)) # 10

print(max(list_a)) # 100

print()
print()

# random library; The random library in Python is a built-in module that provides functions for generating pseudo-random numbers and performing random operations. It is included in the standard library, so no external installation is required.

from random import shuffle # The shuffle() function in Python is part of the random module and is used to randomly reorder the elements of a mutable sequence, such as a list, in place.

list_b = [1,2,3,4,5,6,7,8,9,10]

shuffle(list_b)

print(list_b)

print()
print()

from random import randint # The randint() function in Python is part of the random module and is used to generate a random integer within a specified range, inclusive of both the lower and upper bounds.

print(randint(0,1000))

print()
print()

# the input() function is used to obtain user input from the console. It pauses the program's execution and waits for the user to type something and press Enter.

result = input("What's your name? ")

print(f"Hi {result}, How are ya!!")