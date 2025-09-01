# A for loop in Python is used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence. 

# Example 1

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

print() # Add line break
print() # Add line break


# Example 2

fruits = ("apple","banana","orange","blueberry")

for fruit in fruits:
    print(fruit)

print() # Add line break
print() # Add line break


# Example 3

fruits = ["apple","banana","orange","blueberry"]

for fruit in fruits:
    print("hello")

print() # Add line break
print() # Add line break


# Example 4 (print only even numbers from "mylist")

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")

print() # Add line break
print() # Add line break


# Example 5 (print only odd numbers from "mylist")

for num in mylist:
    if num % 2 != 0:
        print(num)
    else:
        print(f"Even Number: {num}")

print() # Add line break
print() # Add line break


# Example 6 (A sum of all the numbers in mylist using for loop)

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum) # We're running this print statement outside of for loop to get the final result i.e. 55; however, if we want to see a running tally then we run this print statement a part of the for loop as shown in the example below.

print() # Add line break
print() # Add line break


# Example 7

count = 0

for num in mylist:
    count = count + num
    print(count)

print() # Add line break
print() # Add line break


# Example 8

mystring = "Hello World"

for letter in mystring:
    print(letter)

print() # Add line break
print() # Add line break


# Example 9

for letter in "Howdy Fellas!":
    print(letter)

print() # Add line break
print() # Add line break


# Example 10

tup = (1,2,3)

for item in tup:
    print(item)

print() # Add line break
print() # Add line break


# Example 11 - Tuple unpacking

my_tup = [(1,2),(3,4),(5,6),(7,8)]

for elements in my_tup:
    print(elements)

print() # Add line break

# Now we'll unpack the items in tuple

for (a,b) in my_tup:
    print(a)
    print(b)

print() # Add line break

for (a,b) in my_tup:
    print(a)

print() # Add line break

for (a,b) in my_tup:
    print(b)

print() # Add line break
print() # Add line break

# Example 12

d = {"k1":1,"k2":2,"k3":3}

for item in d:
    print(item) # this will output the keys ONLY by default, however to get both key and subsequent values do as follows

print() # Add line break
print() # Add line break


# Example 13

d1 = {"k4":4,"k5":5,"k6":6}

for item in d1.items():
    print(item) # however, below given is how to unpack and access keys and values individually

print() # Add line break

for key,value in d1.items():
    print(value)