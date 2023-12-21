'''
Create a math based game to test a student.
Give them 10 questions to answer.  
You will be graded based on the difficulty of the assignment:
Easy : Computation questions
Medium: Solving one step equations
Hard: Factoring questions
Keep score for the player and play appropriate sound effects when buttons are pressed
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound
from playsound import playsound

win=tk.Tk()



button1=Button(width=6,text='1')
button2=Button(width=6,text='2')
button3=Button(width=6,text='3')
button4=Button(width=6,text='4')
button5=Button(width=6,text='5')
button6=Button(width=6,text='6')
button7=Button(width=6,text='7')
button8=Button(width=6,text='8')
button9=Button(width=6,text='9')
button10=Button(width=6,text='10')

question1=Label(text=' 11 x 16 ')
but1=Button(text='=')
answer1=Entry(width=5)

butList=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10]

def buttfun1(event):
    for i in range(len(butList)):
        butList[i].destroy()
    question1.pack(side=LEFT)
    but1.pack(side=LEFT)
    answer1.pack(side=LEFT)
    butList.remove(button1)

def butans1(event):
    if answer1.get()=='176':
        print('good job')
        playsound('Noises/Meow.mp3',block=FALSE)

    else:
        playsound('Noises/horse.mp3',block=FALSE)

question2=Label(text=' 46 + 47 - 3 x 2')
but2=Button(text='=')
answer2=Entry(width=5)


def buttfun2(event):
    for i in range(len(butList)):
        butList[i].destroy()
    question2.pack(side=LEFT)
    but2.pack(side=LEFT)
    answer2.pack(side=LEFT)
    butList.remove(button2)

def butans2(event,):
    if answer2.get()=='87':
        print('good job')
        playsound('Noises/Meow.mp3',block=FALSE)
        
    else:
        playsound('Noises/horse.mp3',block=FALSE)
        return 0
    

#question1=Label(text=' 11 x 16 ')
#but1=Button(text='=')
#answer1=Entry()


#def buttfun1(event):
#    for i in range(len(butList)):
#        butList[i].destroy()
#    question1.pack(side=LEFT)
#    but1.pack(side=LEFT)
#    answer1.pack(side=LEFT)
#    butList.remove(button1)
#
#def butans1(event):
#    if answer1.get()=='176':
#        print('good job')
#        playsound('Noises/Meow.mp3',block=FALSE)
#    else:
#        playsound('Noises/horse.mp3',block=FALSE)

button1.bind('<Button>',buttfun1)
button2.bind('<Button>',buttfun2)
score1 = but1.bind('<Button>',butans1)
score2 = but2.bind('<Button>',butans2)

button1. grid(column=1,row=1)
button2. grid(column=2,row=1)
button3. grid(column=1,row=2)
button4. grid(column=2,row=2)
button5. grid(column=1,row=3)
button6. grid(column=2,row=3)
button7. grid(column=1,row=4)
button8. grid(column=2,row=4)
button9. grid(column=1,row=5)
button10.grid(column=2,row=5)

win.mainloop()