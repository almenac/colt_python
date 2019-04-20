from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("(enter Player 1's choice): ")

rand_num = randint(1,3)
     


if p2_choice == 1:
    p2_choice = "rock"
elif p2_choice == 2:
    p2_choice == "paper"
elif p2_choice == 3:
    p2_choice == "scissors"

print(p2_choice)

if player == p2_choice:
    print("It's a tie!")
elif p1_choice == "rock":
    if p2_choice == "scissors":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif p1_choice == "paper":
    if p2_choice == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif p1_choice == "scissors":
    if p2_choice == "paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
else:
    print("Something went wrong!")




