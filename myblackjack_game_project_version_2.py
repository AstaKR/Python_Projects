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
    print(logo)
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
 





