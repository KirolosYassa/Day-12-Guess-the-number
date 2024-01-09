import random 
import art
import os 

def guess_game():
    os.system('cls')
    print(art.guess_game_logo)
    type_of_game = input("""
Welcome to the Number Guess Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """)

    choosen_number = random.randint(1, 100)
    user_win_flag = False
    
    attempts = 0
    if type_of_game == 'easy':
        attempts = 10
    elif type_of_game == 'hard':
        attempts = 5
        
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess: "))
        if guessed_number > choosen_number:
            print("Too high!")
        elif guessed_number < choosen_number:
            print("Too low!")
        else:
            print(f"You've got it! the number was {guessed_number}")
            user_win_flag = True
            break
        print("Guess again.")
        attempts -= 1 

    if not user_win_flag:
        print("You've run out of attempts! you lose!")
        print(f"And the chosen number was {choosen_number}")
        
guess_game()