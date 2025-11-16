# Q 1: For nums = [5, 10, 15, 20], print each number multiplied by its index.

nums = [5, 10, 15, 20]

count = 0

for item in nums:
    print(count * item)
    count = count + 1

print()
print()

# Q 2: Write a for loop that prints the numbers from 3 to 8 inclusive.

for num in range(3,9):
    print(num)

print()
print()

# Q 3: Given text = 'bootcamp', print every other character, starting from the first.

text = 'bootcamp'

for c in text[::2]:
    print(c)

print()
print()

# Q 4: For data = [1, 5, 3, 9, 12], print only the numbers greater than 5.

data = [1, 5, 3, 9, 12]

for item in data:
    if item > 5:
        print(item)

print()
print()

# Q 5: For names = ['Amy', 'Ben', 'Cara'], print each name reversed using a loop.

names = ['Amy', 'Ben', 'Cara']

for a in names:
    print(a[::-1])