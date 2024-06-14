from tkinter import * 

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)
def converter():
    mile = int(input_box.get())
    answer = int(mile  * 1.609344)
    answer_label = Label(text=answer)
    answer_label.grid(column=2, row= 2)
    pass
input_box = Entry()
input_box.grid(column=2, row=1)

Mile_label = Label(text="Mile")
Mile_label.grid(column=3, row= 1)

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row= 2)

answer_label = Label(text="")
answer_label.grid(column=2, row= 2)

km_label = Label(text="Km")
km_label.grid(column=3, row= 2)

button = Button(text="Calculate" ,command=converter)
button.grid(column=2, row= 3)

window.mainloop()