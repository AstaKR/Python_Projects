import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dics_data = {row.letter:row.code for (index, row) in data.iterrows()}
# print(dics_data)
def generate_alphabet():
    user_input = input("enter the name : ").upper()

    try:
        user_list = [dics_data[letter] for letter in user_input]

    except KeyError:
        print("Sorry Only enter the Alphabet letters ")
        generate_alphabet()
    else:
        print(user_list)
generate_alphabet()