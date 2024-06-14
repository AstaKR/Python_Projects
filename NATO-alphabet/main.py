import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dics_data = {row.letter:row.code for (index, row) in data.iterrows()}
print(dics_data)


user_input = input("enter the name : ").upper()
user_list = [dics_data[letter] for letter in user_input]

print(user_list)

# print(dict_data)