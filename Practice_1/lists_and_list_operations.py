# Q 1: Given numbers = [3, 7, 1, 9, 12], create a new list with each number squared.

numbers = [3, 7, 1, 9, 12]

new_list = []

for num in numbers:
    new_list.append(num ** 2)

print(new_list)

print()
print()

# Q 2: Given fruits = ['apple', 'banana', 'cherry', 'banana', 'apple'], remove all duplicates while preserving order.

fruits = ['apple', 'banana', 'cherry', 'banana', 'apple']

unique_fruits = []

for f in fruits:
    if f not in unique_fruits:
        unique_fruits.append(f)

print(unique_fruits)

print()
print()

# Q 3: Append the number 20 to numbers = [2, 4, 6, 8] and print the new list.

numbers = [2, 4, 6, 8]

new_list = numbers

new_list.append(20)

print(new_list)

print()
print()

# Q 4: Given sports = ['soccer', 'basketball', 'tennis'], insert the string 'hockey' at index 1.

sports = ['soccer', 'basketball', 'tennis']

sports.insert(1,"hockey")

print(sports)

print()
print()

# Q 5: Given mix = [5, 'cat', 7.1, 'dog'], print only the integer elements.

mix = [5, 'cat', 7.1, 'dog']

int_mix = []

for num in mix:
    if type(num) is int:
        int_mix.append(num)

print(int_mix)