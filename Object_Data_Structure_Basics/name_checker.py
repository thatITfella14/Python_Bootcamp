# This program asks the user for their name and then checks if it is an exact match
# for the preconfigured string "Karan Patel".

# The preconfigured, correct string to check against.
correct_name = "Karan Patel"

# Ask the user for their name.
user_name = input("Please enter your name: ")

# Check if the user's input is an exact, case-sensitive match for the correct name.
if user_name == correct_name:
    # If the names match, print the success message.
    print("Congratulations! You are a human.")
else:
    # If the names do not match, print the failure message.
    print("Fuck off, you bot!")