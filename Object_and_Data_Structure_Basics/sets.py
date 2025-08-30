# Sets are unordered collections of unique elements. Meaning there are no duplicate values.
# They are mutable, meaning you can add or remove elements after creation.

# Creatinng a set

myset = set()  # Empty set

print(myset)  # Output: set()


# Adding object/elements to a set

myset.add(1) # Adding an integer

print(myset)  # Output: {1}

myset.add(2.5) # Adding a float

print(myset)  # Output: {1, 2.5}

myset.add("three") # Adding a string

print(myset)  # Output: {1, 2.5, 'three'}

# FYI, you can only add one element at a time using the add() method.


# Demonstration of uniqueness

myset.add("three") # Trying to add a duplicate element

print(myset)  # Output: {1, 2.5, 'three'} - No change, as 'three' is already in the set


# Since you can only have unique elements in a set - however, you can cast a list with duplicate values to set to find the unique values

mylist = [1,1,1,1,1,2,3,4,4,4,4,5,6,7,8,8,9,9]

print(mylist)  # Output: [1, 1, 1, 1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 9, 9]

print(set(mylist))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9} - Unique values only


# Another example of set returning unique values

print(set('Mississippi'))  # Output: {'M', 'i', 's', 'p'} - Unique characters only