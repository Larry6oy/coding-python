import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL


root = Tk()
root.title('Snap')
c = Canvas(root, width=400, height=400)


shapes = []


circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=NORMAL)
shapes.append(circle)
c.pack()