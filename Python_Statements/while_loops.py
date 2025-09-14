# while loops will continue to execute a code block while some condition remains True.

x = 0

while x <= 5:
    print(f"The current value of x is {x}")
    x = x + 1

print()
print()

# sort of same example as above but I'm going to add an else statement to it

y = 0

while y <= 10:
    print(f"The current value of y is {y}")
    y = y + 1
else:
    print("y NOT LESS THAN OR EQUAL TO 10")


print()
print()

# break, continue, pass ------ we can use break, continue and pass statements in our loops to add additional functionality for various cases

# break: In Python, the break statement is used to immediately terminate the execution of a loop (either a for loop or a while loop). When the break statement is encountered within a loop, the loop is exited, and program execution continues with the statement immediately following the loop.

# continue: The continue statement in Python is used within loops (both for and while loops) to skip the current iteration and move directly to the next iteration of the loop.

# pass: Does nothing at all

# Example of "pass"

x = [1,2,3,4]

for num in x:
    pass

print("end of my script") # look what happened here: the "for" loop iterates through each number in the list 'x'. However, the 'pass' statement is a placeholder that does nothing.So, the loop completes all its cycles without performing any action. After the loop finishes, the next line was executed, which is the print statement "end of my script".

print()
print()

# Example of "continue"

mystring = "Tammy"

for letter in mystring:
    print(letter) # this will iterate through each letter in mystring; however, what if I wanted to skip the letter "a"? Then I'd do as follows

print()
print()

for letter in mystring:
    if letter == "a":
        continue
    print(letter) # now it iterates through mystring but skips "a"

print()
print()

# Example of "break"

name = "Loren"

for letter in name:
    if letter == "e":
        break
    print(letter)

print()
print()

# an example of "break" in while loop

z = 0

while z < 10:
    if z == 7:
        break
    print(z)
    z = z + 1