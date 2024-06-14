from tkinter import *
from random import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
all_data_to_dic = {}
try:
    data = pandas.read_csv("data/learn_to_words.csv")

except:

    data = pandas.read_csv("data/french_words.csv")
    all_data_to_dic = data.to_dict(orient="records")
else:
    all_data_to_dic = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(all_data_to_dic)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(old_pic, image=back_pic)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def delete_word():
    global current_card
    all_data_to_dic.remove(current_card)
    print(len(all_data_to_dic))
    next_card()
    data = pandas.DataFrame(all_data_to_dic)
    data.to_csv("data/learn_to_words.csv", index=False)


window = Tk()
window.title("Flash Card")
window.config(width=800, height=800)

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, )
front_pic = PhotoImage(file="../flash-card-project-start/images/card_front.png")
back_pic = PhotoImage(file="../flash-card-project-start/images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
old_pic = canvas.create_image(400, 250, image=front_pic)
card_title = canvas.create_text(400, 120, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 260, text="", font=("Arial", 20, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_pic = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_pic, width=100, height=100, highlightthickness=0, bg="#B1DDC6", command=next_card)
wrong_button.grid(row=1, column=0, )

right_pic = PhotoImage(file='../flash-card-project-start/images/right.png')
right_button = Button(image=right_pic, highlightthickness=0, width=100, height=100, bg="#B1DDC6", command=delete_word)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
