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

win.geometry('110x200')
win.resizable(FALSE,FALSE)

button1=Button(win,width=6,text='1')
button2=Button(win,width=6,text='2',)
button3=Button(win,width=6,text='3')
button4=Button(win,width=6,text='4')
button5=Button(win,width=6,text='5')
button6=Button(win,width=6,text='6')
button7=Button(win,width=6,text='7')
button8=Button(win,width=6,text='8')
button9=Button(win,width=6,text='9')
button10=Button(win,width=6,text='10')

        
butList=[[button1,0,0],[button2,55,0],[button3,0,30],[button4,55,30],[button5,0,60],[button6,55,60],[button7,0,90],[button8,55,90],[button9,0,120],[button10,55,120]]

question1=Label(text=' 11 x 16 ')
but1=Button(text='=')
answer1=Entry(width=5)

question2=Label(text=' 46 + 47 - 3 x 2')
but2=Button(text='=')
answer2=Entry(width=5)



def butans1(event):
    if answer1.get()=='176':
        print('good job')
        playsound('Noises/Meow.mp3',block=FALSE)
        question1.destroy()
        but1.destroy()
        answer1.destroy()
    else:
        playsound('Noises/horse.mp3',block=FALSE)
        print('badjob')
        question1.destroy()
        but1.destroy()
        answer1.destroy()
        

def buttfun1(event):
    button1.destroy()
    print(butList)
    question1.place(x=0,y=155)
    but1.     place(x=50,y=150)
    answer1.  place(x=75,y=155)

def buttfun2(event):
    button2.destroy()
    question2.place(x=10,y=155)
    but2.place(x=30,y=175)
    answer2.place(x=50,y=180)



def butans2(event):
    if answer2.get()=='87':
        print('good job')
        playsound('Noises/Meow.mp3',block=FALSE)
        question2.destroy()
        but2.destroy()
        answer2.destroy()
    else:
        playsound('Noises/horse.mp3',block=FALSE)
        print('badjob')
        question2.destroy()
        but2.destroy()
        answer2.destroy()
    


button1.bind('<Button>',buttfun1)
button2.bind('<Button>',buttfun2)
but1.bind('<Button>',butans1)
but2.bind('<Button>',butans2)

for i in butList:
    i[0].place(y=i[2],x=i[1])

win.mainloop()