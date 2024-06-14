#Step 1 
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
word_list = ["aardvark", "baboon", "camel"]
chosen_word = str(random.choice(word_list))
print(chosen_word)
lives = 6
choosen_len = len(chosen_word)
display= []
for _ in range(choosen_len):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Enter the Guess word : \n ").lower()
    guess_count = len(guess)   
    if guess in display:
        print("You already guessed this word ")
    for postition in range(choosen_len):
        if guess == chosen_word[postition]:
            display[postition] = guess
    print(display)
    if guess not in chosen_word or guess_count > 1: # if enter the two word in output its showing error -Coding  
        print(f"You guessed {guess}, That's not in the word. You lose a life ")
        lives -=1 
        if lives == 0:
            end_of_game = True
            print("You Lose")
        print(f"You life is {stages[lives]}")
    print(f"{''.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win")


# Output:
 
 
# | |
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |
#                    |___/
# baboon
# ['_', '_', '_', '_', '_', '_']
# Enter the Guess word :
#  camel
# ['_', '_', '_', '_', '_', '_']
# You guessed camel, That's not in the word. You lose a life
# You life is
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# ______
# Enter the Guess word :
#  c 
# ['_', '_', '_', '_', '_', '_']
# You guessed c, That's not in the word. You lose a life
# You life is
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

# ______
# Enter the Guess word :
#  b
# ['b', '_', 'b', '_', '_', '_']
# b_b___
# Enter the Guess word :
#  a
# ['b', 'a', 'b', '_', '_', '_']
# bab___
# Enter the Guess word :
#  o
# ['b', 'a', 'b', 'o', 'o', '_']
# baboo_
# Enter the Guess word :
#  n
# ['b', 'a', 'b', 'o', 'o', 'n']
# baboon
# You win
