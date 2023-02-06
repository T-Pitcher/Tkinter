
# Gives a single roll of a variable-sided dice
# Status: works

from random import randint
from tkinter import Label

from tkinter import *
from random import randint

root = Tk()

display = "-"
sides = 6
font = ("Century", 30)


Display = Label(root, text=display, pady=40, font=font)
Sides = Entry(root, font=font, justify="center")
Sides.insert(0, sides)

def Roll(): 
    sides = int(Sides.get())
    root.title(str(sides)+ "-sided Dice")
    Display.config(text = randint(1,sides))
    
RollButton = Button(root, text="Roll", bg="red", padx = 100, command= Roll, font=font)

Display.grid(row=0)
RollButton.grid(row=1)
Sides.grid(row=2)


root.mainloop()