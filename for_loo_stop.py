n = 10
i = 0
is_game_over = False
while not is_game_over:
    for  i in range(n):
        guess = input("No :")
        if guess == "kali":
            print("You Won")
            break
        else:
            print("again")
    is_game_over = True
        
