# WARMUP SECTION

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

from _ctypes import pointer
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    elif a % 2 != 0 or b % 2 != 0:
        return max(a,b)
    elif a % 2 != 0 and b % 2 != 0:
        return max(a,b)

print()
print()

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(string):
    words = string.split()
    return words[0][0].lower() == words[1][0].lower()

print()
print()

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a,b):
    if a+b == 20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False

print()
print()

# LEVEL 1 PROBLEMS

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

print()
print()

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    result = " ".join(reversed_words)
    return result

print()
print()

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False

# LEVEL 2 PROBLEMS

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for x,y in zip(nums,nums[1:]):
        if x == 3 and y == 3:
            return True
    return False

print()
print()

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    result = ""
    for letter in text:
        result += letter * 3
    return result

print()
print()

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    total = a + b +c
    if total <= 21:
        return total
    if 11 in (a,b,c):
        total = total - 10
    return "BUST" if total > 21 else total

    print()
    print()

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    for num in arr:
        if not (6 <= num <= 9):
            total += num
    return total

print()
print()

# CHALLENGING PROBLEMS

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(arr):
    seq = [0,0,7]
    pointer = 0
    for num in arr:
        if num == seq[pointer]:
            pointer += 1
            if pointer == len(seq):
                return True
    return False