from tkinter import *
import random

root = Tk()

root.title("Dictionary")
root.geometry("600x600")

colors="red","orange","yellow","green","cyan","blue","purple","pink"


def click():
    num = random.randint(0,7)
    picked_color = colors[num]
    root.configure(background=picked_color)

button = Button(root, text="Click Me", command = click)
button.pack()
root.mainloop()