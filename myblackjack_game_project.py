
import random 
# print("Welcome to My Blackjack Game ")
# print("You have $2500 point ")
# Starting_point = 2500
# print(""" 
#   $1  , $10 , $100 , $500
#  """)
# selected_point = int(input("Select your bet points"))

def score_calc(pl_card):
    score = 0
    for i in pl_card:
        score += int(i)
    return score
def new_card(add_card, cards):
    add_card.append(random.choice(Card_values))
    return add_card
def score_print(player_card, computer_card):
    pl_score = score_calc(player_card)
    com_score = score_calc(computer_card)
    print(f"""Your cards : {player_card},     Current_score: {pl_score}""")
    print(computer_card)
    print(f"""Computer's  first card: {computer_card[0]},     Computer's Score: {com_score} """)
    return pl_score , com_score
Card_values= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = []
Computer_card = []
    
def blackjack() :
    
    player_card = random.choices(Card_values ,k =2)
    computer_card = random.choices(Card_values, k =2)
    score_print(player_card, computer_card)    
    key= True
    while key == True:
        options = input("Type 'Y' to get another card, type 'N' to pass :")
        if options == "Y" or options == "y":
            new_pl_card = player_card
            new_comp_card = computer_card
            p_card = new_card(new_pl_card, Card_values)
            c_card = new_card(new_comp_card, Card_values)
            score_point = score_print(p_card, c_card)
            player_point = score_point[0]
            computer_point = score_point[1]
            if player_point == computer_point:
                print("Draw")
            elif player_point > 21:
                print("Score is went over. Computer is win")
            elif computer_point > 21:
                print("Score is went over. Player is win")
            elif player_point > computer_point:
                print("Computer Win")
            else:
                print("Player Win")
        else:
            key = False
    game_start  =input("Do you want play game again y / n")
    if game_start == "y" or "yes" :
        blackjack()
    else:
        key = False
blackjack()