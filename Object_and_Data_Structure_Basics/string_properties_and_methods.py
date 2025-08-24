# Immutability of Strings; it means that once a string is created, it cannot be changed.

name = "Sam"

# If I'd like to change the name to "Pam", I can't do it directly because strings are immutable.
# name[0] = "P"  # This would raise an error

# Instead, I can create a new string based on the old one.

last_letters = name[1:]  # This gets the substring from index 1 to the end

# Now, I can concatenate "P" with last_letters to form the new name

name = "P" + last_letters # this is concatination of strings

print(name)  # Output: Pam


# Another example of string concatenation

my_word = "Hello World"

my_word = my_word + ", it is beautiful outside!"  # Concatenating a new string to x

print(my_word)  # Output: Hello World it is beautiful outside!


# Concatenation that multiplies the string; here's an example

letter = "z"

letter = letter * 10  # This will repeat the string "z" 10 times

print(letter)  # Output: zzzzzzzzzz


# String Methods; these are built-in functions that perform specific operations on strings.

x = "Robert"

print(x.upper())  # Converts all characters in the string to uppercase; Output: ROBERT

print(x.lower())  # Converts all characters in the string to lowercase; Output: robert

y = "Howdy folks"

print(y.split())  # Splits the string into a list of words based on whitespace; Output: ['Howdy', 'folks']

z = "Robert,Hannnah - Claire,John,David-Lee"

print(z.split(","))  # Splits the string into a list based on commas; Output: ['Robert', 'Hannnah - Claire', 'John', ' David-Lee']