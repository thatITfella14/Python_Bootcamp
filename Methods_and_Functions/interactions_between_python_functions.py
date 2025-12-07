# Functions often use results from other functions, let's see a simple example through a guessing game. There will be 3 positions in the list, one of which is an 'J', a function will shuffle the list, another will take a player's guess, and finally another will check to see if it is correct. This is based on the classic carnival game of guessing which cup a red ball is under.

# We'll create a few functions to mimic the carnival guessing game "Three Card Monte". Our simple game won't actually show the cups or ball, instead we'll simply mimic the effect with a python list. Our simple version will also not show the shuffle to the user, so the guess is completely random.

# Step 1: Create a simple list

game_list = [" ","J"," "]

# Step 2: Create a function that shuffles the list

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Step 3: Create a function that takes in the user's guess

def player_guess():

    guess = ""

    while guess not in ["0","1","2"]:
        guess = input("Pick a number: 0, 1, or 2:")
    
    return int(guess)

# Step 4: Write a function that checks to see if the guess is correct

def check_guess(mylist,guess):
    if mylist[guess] == "J":
        print("Correct!")
    else:
        print("Wrong! Better luck next time")

# Step 5: Run all functions

mylist = game_list

shuffle_list(mylist)

guess = player_guess()

check_guess(mylist,guess)