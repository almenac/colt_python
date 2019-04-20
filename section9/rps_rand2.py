from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

p1_choice = input("(enter Player 1's choice): ").lower()

rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}")


if p1_choice == computer:
    print("It's a tie!")
elif p1_choice == "rock":
    if computer == "scissors":
        print("Player wins!")
    else:
        print("Computer wins!")
elif p1_choice == "paper":
    if computer == "rock":
        print("Player wins!")
    else:
        print("Copmuter wins!")
elif p1_choice == "scissors":
    if computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")
else:
    print("Please enter a valid move.")




