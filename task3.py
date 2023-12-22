#
# Create a canvas object and use key bindings to be able to move a sprite around the canvas.
# * Make a sound effect for every time you move the sprite
# * Make a sound effect every time it tries to move off the screen and prevent it from moving off the screen
'''

'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound
from playsound import playsound

from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
x=0
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()