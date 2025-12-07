# Create a number guessing game called "Guess the Secret Number" that mimics a simple casino-style bet where the player tries to guess a randomly generated number between 1 and 5 (inclusive), with the computer providing a hint about whether their guess was too high or too low before revealing the result.

# Step 1: A function called generate_secret() that returns a random integer between 1 and 5 (call random.randint(1, 5) inside it).

from random import randint

def generate_secret():
    secret_num = randint(1,5)
    return secret_num

# Step 2: A function called player_guess() that prompts the user to enter a number between 1 and 5, validates it (using a while loop to reject invalid inputs like 0, 6, or non-numbers), and returns the integer guess.

def player_guess():

    guess = ""

    while guess not in ["1","2","3","4","5"]:
        guess = input("Enter your number: ")

    return int(guess)

# Step 3: A function called check_guess(secret_num, guess) that compares the guess to the secret, prints "Too high!" if the guess > secret, "Too low!" if guess < secret, "Correct! You win!" if equal, or "Wrong guess!" otherwise.

def check_guess(secret_num, guess):
    if guess == secret_num:
        print("Correct!")
    elif guess > secret_num:
        print("Wrong! Too high")
    elif guess < secret_num:
        print("Wrong! Too low")

# Step 4: Run all functions

secret_num = generate_secret()

guess = player_guess()

check_guess(secret_num,guess)