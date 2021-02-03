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
print("-------------------")


#
# determining who won
#



if y == "paper" and x == "scissors":
    print("Congrats! You Won!")
elif y == "scissors" and x == "rock":
    print("Congrats! You Won!")
elif y == "rock" and x == "paper":
    print("Congrats! You Won!")
elif y == x:
    print("It's a tie!")
else:
    print("The computer won. Too bad!")


print("-------------------")
print("Thanks for playing. Please play again!")