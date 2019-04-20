from random import randint

random_number = randint(1,10)
game_over = False

while game_over == False:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess == random_number:
        print("Congratulation! You guessed it!")
        print("The number was: " + str(random_number))
        newgame = input("Do you want to keep playing? y/n")
        if newgame == "y":
            random_number = randint(1,10)
        else:
            game_over = True
    elif guess > random_number:
        print("Too high! Try again!")
    else:
        print("Too low! Try again!")
    

    
        
        
    
