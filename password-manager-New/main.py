from tkinter import *
from tkinter import messagebox
from  random import randint, choice, shuffle
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_text = password_textbox.get()
    if len(password_text) == 0:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # print("Welcome to the PyPassword Generator!")
        # letters_count= int(input("How many letters would you like in your password?\n"))
        # symbols_count = int(input(f"How many symbols would you like?\n"))
        # numbers_count = int(input(f"How many numbers would you like?\n"))
        letters_count = 5
        symbols_count = 5
        numbers_count = 5

        password = [choice(letters) for n in range(randint(8,10))]
        password += [choice(numbers) for n in range(randint(2,4))]
        password += [choice(symbols) for n in range(randint(2,4))]
        output = ""
        # for n in range(1, letters_count + 1 ):
        #     password += random.choice(letters)
        # for n in range(1, numbers_count + 1 ):
        #     password += random.choice(numbers)
        # for n in range (1 , symbols_count + 1):
        #     password += random.choice(symbols)
        # print(password)
        shuffle(password)
        output = "".join(password)

        # print(password)
        # for n in password:
        #     output += n
        password_textbox.insert(0, output)
        pyperclip.copy(output)
    else:

        messagebox.askyesno(title="Oops",message="do you want generate new password ")
        password_textbox.delete(0, END)

        # ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website_name = web_textbox.get()
    email_name = email_textbox.get()
    new_password = password_textbox.get()
    if website_name == "" or new_password == "":
        # if len(website_name) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Warning", message="Kindly Enter the values. ")
    else:
        is_ok = messagebox.askyesno(title=website_name,
                                    message=f"Do you want save following below details \n Username/ Password : {email_name} \n Password: {new_password}")

        if is_ok:
            with open("password.txt", "a") as file:
                file.write(f"{website_name} | {email_name} | {new_password} \n ")
                web_textbox.delete(0, END)
                password_textbox.delete(0, END)
                file.close()


# ---------------------------- UI SETUP ------------------------------- #
FONT = ("Arial", 10, "normal")

window = Tk()
window.config(padx=40, pady=40)
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=img, )
canvas.grid(row=0, column=1)

website = Label(text="Website: ", font=FONT)
website.grid(column=0, row=2)
website.focus()

web_textbox = Entry(width=35, font=FONT)
web_textbox.grid(row=2, column=1, columnspan=2)

email = Label(text="Email / Username: ", font=FONT)
email.grid(column=0, row=3)

email_textbox = Entry(width=35, font=FONT)
email_textbox.grid(column=1, row=3, columnspan=2)
email_textbox.insert(0, "astakr108@gmail.com")

password = Label(text="Password: ", font=FONT)
password.grid(column=0, row=4)

password_textbox = Entry(font=FONT, width=20)
password_textbox.grid(column=1, row=4)
password_generator = Button(text="Generate Password", command=password_generator)
password_generator.grid(row=4, column=2)

add_button = Button(text="ADD", width=36, command=save_file)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
