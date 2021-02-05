# game.py

#loading third party packages
import os
import random

#from dotenv import load_dotenv 
#load_dotenv()  
import dotenv 
dotenv.load_dotenv() 
USER_NAME = os.getenv("PLAYER_NAME", default="Player One")

print("-------------------")
print(f"Welcome '{USER_NAME}' to my Rock-Paper-Scissors game...")
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

rps=['rock', 'paper', 'scissors']

#
#validate the user selection

#stop the program if the user choice is invalid

x.lower()
if x in rps:
    pass
else:
    print("Please choose a valid option and try again!")
    exit()



#y="paper"
#y=computer choice


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
#above solution adapted from Slack from student Estelle Spanneut


print("-------------------")
print("Thanks for playing. Please play again!")