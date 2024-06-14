logo = """


  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _ ___ ___ _   _ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | / __/ __| | | | | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| \__ \__ \ |_| | | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|___/___/\__,_|_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               

"""
import random 
EASY_MODE = 10
HARD_MODE = 5
turns = 0
print(logo)
print("Welcome to Number Guessing Game")

def guess(guess, guessed_no, turns):
    if guessed_no < guess:
        print("Your Guessed higher")
        return turns - 1
    elif guessed_no > guess:
        print("You guessed Lower`")
        return turns - 1
    else:
        print(f"You guessed Coreect{guessed_no}")

def game_modes(mode):
    turns = 0
    if mode == "easy" :
        turns = EASY_MODE
        return turns
    else:
        turns = HARD_MODE
        return turns
def game():      
    print("I'm thinging of a number between 1 and 100. ")
    guessed_number = random.randrange(1,100)
    game_mode = input("Choose a difficultly. Type 'easy' or 'hard' :")
    turn = game_modes(game_mode)
    guessing = 0
    while guessing != guessed_number :
        print(guessed_number)
        print(f"You have {turn} remaining the guessing the numbers")
        guessing = int(input("Enter the guess number:"))
        turn = guess(guessing , guessed_number, turn)
        if turn == 0 :
            print("You've run out of guesses, you lose.")
            return 
        elif guessing != guessed_number:
            print("Guess again") 
game()