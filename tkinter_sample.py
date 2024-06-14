from tkinter import *

window = Tk()
window.title("First window ")
window.minsize(width=500, height=400)

label_1 = Label(text= "" , font=("Arial", 20, "bold"))
label_1.pack()

label_1["text"] = ""
label_1.config(text="New text")
def button_clicked():
    # print("button is clicked")
    # output_label = Label(text="i got clicked" ,font=("arrial", 10, "normal"))
    # output_label.pack(side="bottom")
    # label_1.config(text="I got Clicked ")
    # label_1.config(text=text_box.get())
    new_label = text_box.get()
    label_1.config(text=new_label)
text_box = Entry()
text_box.pack()

button_cl = Button(text="click me", command=button_clicked, background="red")
button_cl.pack()








window.mainloop()
