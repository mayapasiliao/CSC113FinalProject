from tkinter import *

def callback():
    n.get()
    print(n)

master = Tk()
master.title("Input")
Label(master, text="Enter n, number of most common characters: ").grid(row=1)
e1 = Entry(master)
e1.grid(row=1, column=1)
button = Button(master, text="Enter", command = probability(n.get())
button.grid(row=2, column=0, pady=4, textvariable = n)

mainloop()
