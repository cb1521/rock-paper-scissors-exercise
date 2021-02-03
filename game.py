# game.py

import random

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
#asking a user for an input
#

x=input("Please choose either 'rock', 'paper', or 'scissors': ")

#x=user choice

#print(x)
print("You chose:",x)

#string interpolation
#print(f"You chose: {x}")


#y="paper"
#y=computer choice


rps=['rock', 'paper', 'scissors']
y=random.choice(rps)

print("The computer chose:",y)


exit()




















print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")