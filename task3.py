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

win=tk.Tk()

button1=Button(width=6,text='1')
button2=Button(width=6,text='2',)
button3=Button(width=6,text='3')
button4=Button(width=6,text='4')
button5=Button(width=6,text='5')
button6=Button(width=6,text='6')
button7=Button(width=6,text='7')
button8=Button(width=6,text='8')
button9=Button(width=6,text='9')
button10=Button(width=6,text='10')

butList=[[button1,0,0],[button2,55,0],[button3,0,30],[button4,55,30],[button5,0,60],[button6,55,60],[button7,0,90],[button8,55,90],[button9,0,120],[button10,55,120]]


win.mainloop()