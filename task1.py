'''

Create a sound board.
This is a collection of buttons that is each bound to a sound effect.
These are great ways to help teach little children the different sounds that 
animals make, especially if you can add an image of the animal to the button.
You can choose what sound effects to include in your sound board.  Early sound 
boards were just sampled music bound to electronic keyboards: https://www.youtube.com/watch?v=z0PJnc8BFTk
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound
from playsound import playsound

win=tk.Tk()

def catSound(event):
    playsound('Noises/Meow.mp3',block=FALSE)
def dogSound(event):
    playsound('Noises/Dog1.mp3',block=FALSE)
def horSound(event):
    playsound('Noises/Horse.mp3',block=FALSE)
def seaSound(event):
    playsound('Noises/Seagulls (1).mp3',block=FALSE)


Instructions=Label(height=3,font=('',26),text='Animal Soundboard')
catPic=PhotoImage(file='Noises/cat.png')
dogPic=PhotoImage(file='Noises/dog.png')
horPic=PhotoImage(file='Noises/horse.png')
seaPic=PhotoImage(file='Noises/seagull.png')

catBut=Button(height=140,width=120,text='Cat',image=catPic,compound=TOP,font=('',15))
dogBut=Button(height=140,width=120,text='Dog',image=dogPic,compound=TOP,font=('',15))
horBut=Button(height=140,width=120,text='Horse',image=horPic,compound=TOP,font=('',15))
seaBut=Button(height=140,width=120,text='Seagull',image=seaPic,compound=TOP,font=('',15))

catBut.bind('<Button>',catSound)
dogBut.bind('<Button>',dogSound)
horBut.bind('<Button>',horSound)
seaBut.bind('<Button>',seaSound)

Instructions.grid(column=2,columnspan=2,row=1)
catBut.grid(column=1,row=2)
dogBut.grid(column=2,row=2)
horBut.grid(column=3,row=2)
seaBut.grid(column=4,row=2)

win.mainloop()