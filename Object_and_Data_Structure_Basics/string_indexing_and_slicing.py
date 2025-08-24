# Indexing - Accessing individual characters in a string using their position (index).

my_string = "Hello World"

print(my_string[0]) #H

print(my_string[8]) #r

print(my_string[9]) #l

print(my_string[-2]) #l; this is negative indexing (or I can say reverse indexing)


# Reassignment of string

my_string = "abcdefghijk"

print(my_string)


# Slicing - Extracting a substring from a string using a range of indices.

print(my_string[2:]) #cdefghijk; from index 2 to end

print(my_string[:7]) #abcdefg; from start to index 6


# Slicing a substring

print(my_string[3:6]) #def; from index 3 to index 5

print(my_string[3:9]) # defghi; from index 3 to index 8


# Step in slicing; step defines the increment between each index in the specified range.

print(my_string[::2]) #acegik; from start to end with a step of 2

print(my_string[2:7:2]) #ceg; from index 2 to index 6 with a step of 2

print(my_string[::-1]) # Reversing a string using slicing