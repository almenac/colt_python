from random import randint

player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player score: {player_wins}, Computer score: {computer_wins}")    
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    player = input("Player, make your move: ").lower()
    rand_num = randint(0,2)
    if player == "quit" or player == "q":
        break
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}" )

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")	
            computer_wins += 1
    else:
        print("Please enter a valid move!")
if player_wins > computer_wins:
    print("Congratulations, player won!")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("Waah, waah! Computer won!")

print("Final scores:")
print(f"Player score: {player_wins}, Computer score: {computer_wins}")    