from tkinter import  *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reprs = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_label, text="00:00")
    title_label.config(text="Timer")
    tick.config(text="")
    global reprs
    reprs = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global  reprs
    reprs +=1
    work_sec = WORK_MIN * 60
    short_time_break = SHORT_BREAK_MIN * 60
    big_time_break = LONG_BREAK_MIN * 60

    if reprs % 8 == 0:
        count_down(big_time_break)
        title_label.config(text="BREAK TIME", fg=RED )
    elif reprs % 2 == 0:
        count_down(short_time_break)
        title_label.config(text="BREAK TIME", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK TIME" , fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reprs/2)):
            marks += "✔"
            tick.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=YELLOW)
title_label = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title_label.grid(row=1, column=2)

#image
canvas = Canvas(window, width=220, height=230, bg=YELLOW, highlightthickness=0)
canvas_pic = PhotoImage(file="tomato.png")
img = canvas.create_image(102 , 112 , image=canvas_pic)
timer_label = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="START", bg=YELLOW, command=start_timer)

start_button.grid(row=3, column=1)

reset_button = Button(text="RESET" , bg=YELLOW ,command=reset_timer)
reset_button.grid(row=3, column=3)

tick = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
tick.grid(row=3, column=2)



window.mainloop()