import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose ? 0 for Racks , 1 for Papers and 2 for Scissor"))
if user_choice >2 or user_choice <=-1:
    print("User input is invalid. User is lose the Game")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Choice is ")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("User is won the Game ")
    elif user_choice == 2 and computer_choice ==1:
        print("User is won the Game")
    elif user_choice == 1 and computer_choice == 0:
        print("User is won the Game")
    elif user_choice == computer_choice:
        print("This is draw")
    else:
        print("You lose the Game")
