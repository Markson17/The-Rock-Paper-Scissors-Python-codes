import random
print("The Rock-Paper-Scissors Python Game")
print('Instructions: \nR for rock \nP for paper \nS for scissors')

user_action = input("Enter a choice(R , P or S): ").upper()
possible_options = ["Rock", "Paper", "Scissors"]
computer_action = random.choice(possible_options)

while True:
    if user_action == "R":
        user_action = "Rock"
    elif user_action == "P":
        user_action = "Paper"
    elif user_action == "S":
        user_action = "Scissors"
    elif  user_action not in  possible_options:
        print("You put in an invalid option")
        user_action = input("Enter a choice(R , P or S): ").upper()

    elif user_action == computer_action:
        print(f"Player({user_action}): CPU({computer_action})")
        print(f"Both players selected {user_action}, therefore it'a tie!")
        print("Play again")
        user_action = input("Enter a choice(R , P or S): ").upper()
        computer_action = random.choice(possible_options)
        continue
    else:
        print(f"Player({user_action}): CPU({computer_action})")

        if user_action == "Rock":
            if computer_action == "Scissors":
                print("Rock smaches scissors! You win!")
            else:
                print("Paper covers rock! You lose!.")

        elif user_action == "Paper":
            if computer_action == "Rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose!")

        elif user_action == "Scissors":
            if computer_action == "Paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose!")
        print("Game Over!")
        break




    



