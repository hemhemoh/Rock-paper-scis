import random

while True:
    valid_inputs = ["rock", "paper", "scissors"]
    computer_input = random.choice(valid_inputs)
    user_input = input("Please pick between rock, paper and scissors \n").lower()

    if user_input not in valid_inputs:
        print("Please enter either rock, paper or scissors ")
    else:
        print(f"\nYou chose {user_input}, computer chose {computer_input}.\n")
        if user_input == computer_input:
            print(f"Both user selected {user_input} and that is a tie")
        elif computer_input == "rock":
            if user_input == "scissors":
                print("The computer inputed rock, you lose")
            else:
                print("The computer inputed rock and you inputed paper, you win!")
        elif computer_input == "paper":
            if user_input == "scissors":
                print("The computer inputed paper and you just cut the paper away, so you win!!")
            else:
                print("Paper covers rock, so you lose")
        elif computer_input == "scissors":
            if user_input == "paper":
                print("The computer inputed scissors and has cut you away. You lose")
            else:
                print("You smashed the computer's scissors, you win!!")
        try_again = input("Do you want to play again?\n").lower()
        if try_again[0]  != "y":
            break
