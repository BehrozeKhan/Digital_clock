
print("Digital clock and date in Tkinter Python")
from tkinter import *
from tkinter import ttk
from tkinter import font

import time
import datetime

def quit(*args):
	root.destroy()


def digitalclock():
	time = datetime.datetime.now()
	date = datetime.date.today()
	date = date.strftime("%d-%m-%Y %a")
	time = time.strftime("%I:%M:%S %p")
	txt.set(date)
	txt1.set(time)
	root.after(1000,digitalclock)


root = Tk()
root.attributes('-fullscreen', True)
root.configure(background="#000000")
root.bind("<Escape>",quit)
root.after(0,digitalclock)

fnt = font.Font(family='Colonna MT Regular', size=120, 
	weight='bold')

txt = StringVar()
txt1 = StringVar()

clock = ttk.Label(root, foreground="#ffffff" , textvariable=txt,
	font=fnt,background="#000000")
clock1 = ttk.Label(root, foreground="#ffffff" , textvariable=txt1,
	font=fnt,background="#000000")

clock.pack()
clock1.pack()

root.mainloop()
