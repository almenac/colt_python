print("...rock...")
print("...paper...")
print("...scissors...")

p1_choice = input("(enter Player 1's choice): ")
print("***NO CHEATING!***\n\n" * 40)
p2_choice = input("(enter Player 2's choice): ")

#ongelmana virheenkäsittely

if p1_choice == p2_choice:
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




