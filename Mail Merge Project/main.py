
PLACE_HOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    letters = letter.read()
    
    for name in names:
        letters = letters.split("\n")
        new_letter = letters.replace(PLACE_HOLDER, name)
        print(new_letter)




