from tkinter import *
from Turtle import draw_pie_chart

# Sample function
def callback():
   draw_pie_chart(int(e1.get()))

master = Tk()
master.title("Input")

Label(master, text="Enter n, number of most common characters: ").grid(row=0)

e1 = Entry(master)
e1.grid(row=0, column=1)

Button(master, text="Quit", command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text="Enter", command=callback).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
