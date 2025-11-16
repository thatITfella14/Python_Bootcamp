# Q 1: Given num = 18, print True if num is even, otherwise print False.

num = 18

print(num % 2 == 0)

print()
print()

# Q 2: For age = 20, print 'Adult' if age is 18 or over, 'Teenager' if age is 13–17, and 'Child' if younger.

age = 20

if age >= 18:
    print("Adult")
elif age >=13 and age <= 17:
    print("Teenager")
elif age < 13:
    print("Child")

print()
print()

# Q 3: Given word = 'Python', print True if it starts with a capital letter, otherwise False (use code to check).

word = "Python"

print(word[0].isupper())

print()
print()

# Q 4: If temperature = 28, print 'Cold' if below 10, 'Warm' if 10–25 (inclusive), 'Hot' if above 25.

temperature = 28

if temperature < 10:
    print("Cold")
elif temperature >= 10 and temperature <= 25:
    print("Warm")
elif temperature > 25:
    print("Hot")

print()
print()

# Q 5: Given list1 = [2, 4, 6] and list2 = [1, 4, 7], print True if the lists share any elements.

list1 = [2, 4, 6]

list2 = [1, 4, 7]

found = False

for item in list1:
    if item in list2:
        found = True
        break

print(found)