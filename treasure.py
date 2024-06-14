line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
position = input()
letter = position[0].lower()
abc = [ "a", "b", "c" ]
print(letter)
letter_index = abc.index(letter)
number_index = int(position[1]) -1
map[number_index][letter_index]  = "X"
print(f"{line1} \n {line2}\n {line3} ")