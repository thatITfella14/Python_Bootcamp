# Tuples are immutable sequences, typically used to store collections of heterogeneous data
# Tuples are defined by enclosing the elements in parentheses ( ) and separating them with commas
# Difference between tuples and lists is that tuples cannot be changed (immutable) while lists can be changed (mutable)

t = (1,2,3)

mylist = [1,2,3]

print(type(t))

print(type(mylist))


# Just like lists, tuples can store heterogeneous (diverse) data types

t1 = (1,"two",3)

print(t1[2])


# Tuples have two different methods; count and index

t2 = (1,2,3,1,1,1)

print(t2.count(1))  # counts how many times 1 appears in the tuple

print(t2.index(3))  # returns the index of the first occurrence of 3 in the tuple


# Demonstrating immutability of tuples

mylist[0] = "one"  # This works because lists are mutable

print(mylist)

t2[0] = "one"  # This will raise an error because tuples are immutable

print(t2)