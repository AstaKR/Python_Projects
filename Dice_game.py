import random
print("""
            Welcone to Dice Game
""")

print("""
    Rule: Whoever reaches the goal value first wins. 

""")

def select_dice():
    no =  int(random.randint(1 ,6))
    return no

def print_dice(no):
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")  

    
target_score = int(input("Choose the target points : "))
is_game_over = False
player_score = 0
computer_score = 0
while not is_game_over == True: 
    choice = input("Do you ready to dice : type y or n to continue : ").lower()
    print(choice)
    if choice == "y":
        new_player_dice = select_dice()
        new_computer_dice = select_dice()
        print("Player dice is " )
        print_dice(new_player_dice)
        print("Computer dice is ")
        print_dice(new_computer_dice)
        print(f"Player score is {new_player_dice}  Computer Score is {new_computer_dice}") 
        player_score += new_player_dice
        computer_score +=new_computer_dice
        print(player_score)
        print(computer_score)
        if player_score == target_score and  computer_score == target_score:
            print("Game is draw")
            is_game_over = True
        elif player_score >= target_score:
            print("Player won the game")
            is_game_over = True
        elif computer_score >= target_score:
            print("Computer won the Game ")
            is_game_over = True    
    else:
        print("Player the exit the game")
        is_game_over = True

# Output:

#             Welcone to Dice Game


#     Rule: Whoever reaches the goal value first wins. 


# Choose the target points : 10
# Do you ready to dice : type y or n to continue : y
# y
# Player dice is
# [-----]
# [ 0   ]
# [     ]
# [   0 ]
# [-----]
# Computer dice is
# [-----]
# [0   0]
# [     ]
# [0   0]
# [-----]
# Player score is 2  Computer Score is 4
# 2
# 4
# Do you ready to dice : type y or n to continue : y
# y
# Player dice is
# [-----]
# [     ]
# [  0  ]
# [     ]
# [-----]
# Computer dice is
# [-----]
# [0   0]
# [  0  ]
# [0   0]
# [-----]
# Player score is 1  Computer Score is 5
# 3
# 9
# Do you ready to dice : type y or n to continue : y
# y
# Player dice is
# [-----]
# [     ]
# [  0  ]
# [     ]
# [-----]
# Computer dice is
# [-----]
# [0 0 0]
# [     ]
# [0 0 0]
# [-----]
# Player score is 1  Computer Score is 6
# 4
# 15
# Computer won the Game
         

