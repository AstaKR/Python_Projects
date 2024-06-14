import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    letters_count= int(input("How many letters would you like in your password?\n"))
    symbols_count = int(input(f"How many symbols would you like?\n"))
    numbers_count = int(input(f"How many numbers would you like?\n"))
    password = [random.choice(letters) for n in range(1, letters_count+1)]
    password += [random.choice(numbers) for n in range(1, numbers_count + 1)]
    password += [random.choice(symbols) for n in range(1, symbols_count +1 )]
    output = ""
    # print(password)
    random.shuffle(password)
    # print(password)
    for n in password:
        output += n
    print(output)

kali = password_generator()


# Output:
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 3
# How many symbols would you like?
# 1
# How many numbers would you like?
# 2
# 8sO2$X