# 1

st = "Print only the words that start with s in this sentence"

for letter in st.split():
    if letter[0] == "s":
        print(letter)

print()
print()

# 2

for num in range(0,11):
    if num % 2 == 0:
        print(num)

print()
print()

# 3

mylist = [num for num in range(1,51) if num % 3 == 0]

print(mylist)

print()
print()

# 4

st = 'Print every word in this sentence that has an even number of letters'

for letter in st.split():
    if len(letter) % 2 == 0:
        print("even")
    else:
        print(letter)

print()
print()

# 5

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print()
print()

# 6

st = 'Create a list of the first letters of every word in this string'

list_a = [letter[0] for letter in st.split()]

print(list_a)