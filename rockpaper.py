import random
user_choice=int(input("Enter your choice: Type 0 for ROCK, Type 1 for PAPER, Type 2 for SCISSORS."))
if user_choice >=3 or user_choice < 0:
    print("You've entered invalid number, so you lose")
else:
    computer_choice = random.randint(0,2)
    print("Computer Chose: ")
    print(computer_choice)
    if computer_choice == user_choice:
        print("Its a draw")
    elif computer_choice == 0 & user_choice == 2:
        print("You Loose")
    elif user_choice == 0 & computer_choice == 2:
        print("You Win")
    elif computer_choice > user_choice:
        print("You Loose")
    elif user_choice > computer_choice:
        print("You Win")
