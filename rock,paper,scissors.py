import random
from tkinter import N
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    print(computer)
    while player not in choices:
        player =  input("'rock','paper','scissors'?: ").lower()

    if player == computer:
        print("player: ",player)
        print("computer: ", computer)
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("player: ",player)
            print("computer: ", computer)
            print("You loose!")
        if computer == "sccissors":
            print("player: ",player)
            print("computer: ", computer)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("player: ",player)
            print("computer: ", computer)
            print("You loose!")
        if computer == "paper":
            print("player: ",player)
            print("computer: ", computer)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("player: ",player)
            print("computer: ", computer)
            print("You loose!")
        if computer == "rock":
            print("player: ",player)
            print("computer: ", computer)
            print("You win!")

    play_again = input("play again?(Yes/No)").lower()
    if play_again != "yes":
        break
print("Bye!")

    
