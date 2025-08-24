# .format() method of strings
# The .format() method of strings allows you to insert values into a string
# at specific placeholders defined by curly braces {}.
# This method is useful for creating dynamic strings with variable content.

# Example 1: Basic usage of .format()

print("This is a string {}".format('INSERTED'))  # Output: This is a tring INSERTED

print("Hello, {}. Welcome to the {}".format('Alice', 'Wonderland'))  # Output: Hello, Alice. Welcome to the Wonderland


# Example 2: Indexed placeholders

print("The {} {} {}".format('fox', 'quick', 'brown'))  # Output: The fox brown quick; order is based on the order of arguments

print("The {1} {2} {0}".format('fox', 'quick', 'brown')) # Output: The quick brown fox; order is based on the indices provided in the placeholders

print("The {1} {2} {0}, is a bad {0} :(".format('fox', 'quick', 'brown')) # Output: The quick brown fox, is a bad fox; the first argument is reused


# Examplle 3: Named placeholders

print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))  # Output: The quick brown fox; order is based on the names provided in the placeholders


# Float formatting with .format()
# The float fomatting follows "{value:width.precision f}"
# where width is the total number of characters (including the decimal point)
# and precision is the number of digits to display after the decimal point.
# If width is not specified, it defaults to the minimum required width.
# If precision is not specified, it defaults to 6.

result = 100/777

print("The result was {r}".format(r = result))  # Output: The result was 0.1287001287001287

print("The result was {r:1.3f}".format(r = result))  # Output: The result was 0.129; rounded to 3 decimal places

print("The result was {r:20.3f}".format(r = result)) # Output: The result was                0.129; total width is 20 characters, padded with spaces on the left


# f strings (formatted string literals)
# f strings are a more modern way to format strings in Python (introduced in Python 3.6).
# They are prefixed with 'f' or 'F' and allow you to embed expressions directly within string literals.
# This method is often more readable and concise than using the .format() method.

name = "Robert"

print(f"The guy's name is {name}.")  # Output: The guy's name is Robert.

# Another example with f strings

my_name = "John"
my_age = 46

print(f"Hello! My name's {my_name} and I'm {my_age} years old.")  # Output: Hello! My name's John and I'm 46 years old.