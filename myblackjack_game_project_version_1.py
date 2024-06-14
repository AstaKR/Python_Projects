
# import random 
# # print("Welcome to My Blackjack Game ")
# # print("You have $2500 point ")
# # Starting_point = 2500
# # print(""" 
# #   $1  , $10 , $100 , $500
# #  """)
# # selected_point = int(input("Select your bet points"))

# def score_calc(pl_card):
#     score = 0
#     for i in pl_card:
#         score += int(i)
#     return score
# def new_card(add_card, cards):
#     add_card.append(random.choice(Card_values))
#     return add_card
# def score_print(player_card, computer_card):
#     pl_score = score_calc(player_card)
#     com_score = score_calc(computer_card)
#     print(f"""Your cards : {player_card},     Current_score: {pl_score}""")
#     print(computer_card)
#     print(f"""Computer's  first card: {computer_card[0]},     Computer's Score: {com_score} """)
#     return pl_score , com_score
# Card_values= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# player_card = []
# Computer_card = []
    
# def blackjack() :
    
#     player_card = random.choices(Card_values ,k =2)
#     computer_card = random.choices(Card_values, k =2)
#     score_print(player_card, computer_card)    
#     key= True
#     while key == True:
#         options = input("Type 'Y' to get another card, type 'N' to pass :")
#         if options == "Y" or options == "y":
#             new_pl_card = player_card
#             new_comp_card = computer_card
#             p_card = new_card(new_pl_card, Card_values)
#             c_card = new_card(new_comp_card, Card_values)
#             score_point = score_print(p_card, c_card)
#             player_point = score_point[0]
#             computer_point = score_point[1]
#             if player_point == computer_point:
#                 print("Draw")
#             elif player_point > 21:
#                 print("Score is went over. Computer is win")
#             elif computer_point > 21:
#                 print("Score is went over. Player is win")
#             elif player_point > computer_point:
#                 print("Computer Win")
#             else:
#                 print("Player Win")
#         else:
#             key = False
#     game_start  =input("Do you want play game again y / n")
#     if game_start == "y" or "yes" :
#         blackjack()
#     else:
#         key = False
# blackjack()



############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.      

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
print(logo)
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def dick(cards):
    return random.choice(cards)
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def score_cal(score):
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(score) == 21 and len(score) == 2 :
        return 0
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in score and sum(score) >21:
        score.remove(11)
        score.append(1)   
    return sum(score)
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. 
# If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. 
# If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. 
# If none of the above, then the player with the highest score wins.
def compare(p_score , comp_score):
    if p_score > 21 and comp_score > 21 :
        print("Your score is went over. You lose")
    elif p_score == comp_score :
        print("Game is Draw ")
    elif comp_score == 0 :
        print("Computer is win the game. Computer has Blockjack")
    elif p_score == 0:
        print("Player is win the game. Player has Blackjack")
    elif p_score > 21 :
        print("Your score went over . Player is lose the game ")
    elif comp_score > 21 :
        print("Computer score is went over . Player is win")
    elif p_score > comp_score:
        print(" You won the game ")
    else: 
        print("You lose the game ")

def play_game():
    card_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card = []
    computer_card = []
    is_game_over = False
    for _ in range(2):
        player_card.append(dick(card_value))
        computer_card.append(dick(card_value))
    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
        pl_score = score_cal(player_card)
        comp_score = score_cal(computer_card)
        print(f"    Your's Card is {player_card}    Your's Score is {pl_score}")
        print(f"Computer Card is {computer_card[0]}")
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if pl_score == 0 or comp_score == 0 or pl_score > 21:
            is_game_over = True
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. 
    # If no, then the game has ended.

        else: 
            user_choice = input("Do you want to get another cards  type 'y' or 'n'").lower()
            if user_choice == "y" or user_choice == "yes":
                player_card.append(dick(card_value))
                # computer_card.append(dick(card_value))
            else:
    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.      
                is_game_over = True
    while comp_score != 0 and comp_score < 17 :
        computer_card.append(dick(card_value))
        comp_score = score_cal(computer_card)

    print(f" Yours Card is : {player_card}           Your's Final Score is {pl_score} ")
    print(f" Computer Card is: {computer_card}        Computer Score is : {comp_score}")
    print(compare(pl_score, comp_score))
while input("Do you want play again type y or no :").lower() == "y":
    play_game()
 





