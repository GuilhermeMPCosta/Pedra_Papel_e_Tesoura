from optparse import Option
import random

user_win=0
computer_win=0

options = ["rock", "paper","scissors"]
options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in ["rock", "paper","scissors"]:
        continue    

    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_win += 1
    elif user_input == "scissors" and computer_pick == "papers":
        print("You Won")
        user_win += 1
    else:
        print("You Lost")
        computer_win += 1   

print("User won", user_win, "times")
print("Computer won", computer_win, "times")
print("GoodBye" )
