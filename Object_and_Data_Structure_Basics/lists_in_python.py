# List concatenation

my_list = ['one', 2, 'three', 4.0]

another_list = ['five', 6, 'seven', 8.0]

new_list = my_list + another_list

print(new_list)


# List mutation; elements can be changed in a list but cannot be changed in a string.

new_list[0] = 'ONE ALL CAPS'

print(new_list)


# Appending to a list

new_list.append(9)

print(new_list)


# Removing from a list; "pop" removes the last element in the list

new_list.pop()

print(new_list) # 9 is removed

# Example of removing a specific element in a list

new_list.pop(0) # removes the first element in the list

print(new_list) # 'ONE ALL CAPS' is removed


# Sorting a list

list1 = ['c', 'e', 'x', 'a', 'z', 'r']

num_list = [4, 1, 3, 2, 5]

list1.sort()

num_list.sort()

print(list1)

print(num_list)


# Reversing a list

print(num_list)

num_list.reverse()

print(num_list)