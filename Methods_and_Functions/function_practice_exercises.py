# WARMUP SECTION

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

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