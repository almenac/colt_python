from random import randint

random_number = randint(1,10)
game_over = False

while game_over == False:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > random_number:
        print("Too high! Try again!")
    elif guess < random_number:
        print("Too low! Try again!")
    else:
        print("Congratulation! You guessed it!")
        newgame = input("Do you want to keep playing? y/n")
        if newgame == "y":
            random_number = randint(1,10)
        else:
            game_over = True
        
    
