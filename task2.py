'''
Create a math based game to test a student.
Give them 10 questions to answer.  
You will be graded based on the difficulty of the assignment:
Easy : Computation questions
Medium: Solving one step equations
Hard: Factoring questions
Keep x for the player and play appropriate sound effects when buttons are pressed
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound
from playsound import playsound

win=tk.Tk()

win.geometry('110x200')
win.resizable(FALSE,FALSE)

x = 0

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

question2=Label(text=' 46 + 47 - 3 x 2 ')
but2=Button(text='=')
answer2=Entry(width=5)


question3=Label(text=' (5 + 22 / 2) / 2 ')
but3=Button(text='=')
answer3=Entry(width=5)

question4=Label(text=' 2 * sin(30deg) ')
but4=Button(text='=')
answer4=Entry(width=5)

question5=Label(text=' sqrt(3^2+4^2) ') 
but5=Button(text='=')
answer5=Entry(width=5)

question6=Label(text=' 42 / 36 x 3')
but6=Button(text='=')
answer6=Entry(width=5)

question7=Label(text=' 5!') 
but7=Button(text='=')
answer7=Entry(width=5)

question8=Label(text=' 6^3') 
but8=Button(text='=')
answer8=Entry(width=5)

question9=Label(text=' 6.02 x 10^3') 
but9=Button(text='=')
answer9=Entry(width=5)

question10=Label(text=' (70 - 42) / (84 / 12)') 
but10=Button(text='=')
answer10=Entry(width=5)


def butans1(event):
    global x
    if answer1.get()=='176':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question1.destroy()
        but1.destroy()
        answer1.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question1.destroy()
        but1.destroy()
        answer1.destroy()

def butans2(event):
    global x
    if answer2.get()=='87':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question2.destroy()
        but2.destroy()
        answer2.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question2.destroy()
        but2.destroy()
        answer2.destroy()

def butans3(event):
    global x
    if answer3.get()=='18':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question3.destroy()
        but3.destroy()
        answer3.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question3.destroy()
        but3.destroy()
        answer3.destroy()

def butans4(event):
    global x
    if answer4.get()=='1':
        x=x+1
        print(f'Score: {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question4.destroy()
        but4.destroy()
        answer4.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question4.destroy()
        but4.destroy()
        answer4.destroy()

def butans5(event):
    global x
    if answer5.get()=='5':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question5.destroy()
        but5.destroy()
        answer5.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question5.destroy()
        but5.destroy()
        answer5.destroy()

def butans6(event):
    global x
    if answer6.get()=='3.5':
        x=x+1
        print('Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question6.destroy()
        but6.destroy()
        answer6.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question6.destroy()
        but6.destroy()
        answer6.destroy()

def butans7(event):
    global x
    if answer7.get()=='120':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question7.destroy()
        but7.destroy()
        answer7.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question7.destroy()
        but7.destroy()
        answer7.destroy()

def butans8(event):
    global x
    if answer8.get()=='216':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question8.destroy()
        but8.destroy()
        answer8.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question8.destroy()
        but8.destroy()
        answer8.destroy()

def butans9(event):
    global x
    if answer9.get()=='6020':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question9.destroy()
        but9.destroy()
        answer9.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question9.destroy()
        but9.destroy()
        answer9.destroy()

def butans10(event):
    global x
    if answer10.get()=='4':
        x=x+1
        print(f'Score : {x}')
        playsound('Noises/Coin2.wav',block=FALSE)
        question10.destroy()
        but10.destroy()
        answer10.destroy()
    else:
        playsound('Noises/Loss.wav',block=FALSE)
        print(f'Incorrect. Score : {x}')
        question10.destroy()
        but10.destroy()
        answer10.destroy()



def buttfun1(event):
    button1.destroy()
    question1.place(x=30,y=155)
    but1.     place(x=30,y=175)
    answer1.  place(x=50,y=180)

def buttfun2(event):
    button2.destroy()
    question2.place(x=10,y=155)
    but2.     place(x=30,y=175)
    answer2.  place(x=50,y=180)

def buttfun3(event):
    button3.destroy()
    question3.place(x=10,y=155)
    but3.     place(x=30,y=175)
    answer3.  place(x=50,y=180)

def buttfun4(event):
    button4.destroy()
    question4.place(x=10,y=155)
    but4.     place(x=30,y=175)
    answer4.  place(x=50,y=180)

def buttfun5(event):
    button5.destroy()
    question5.place(x=10,y=155)
    but5.     place(x=30,y=175)
    answer5.  place(x=50,y=180)

def buttfun6(event):
    button6.destroy()
    question6.place(x=20,y=155)
    but6.place(x=30,y=175)
    answer6.place(x=50,y=180)

def buttfun7(event):
    button7.destroy()
    question7.place(x=10,y=155)
    but7.place     (x=30,y=150)
    answer7.place  (x=55,y=155)

def buttfun8(event):
    button8.destroy()
    question8.place (x=10,y=155)
    but8.place      (x=50,y=150)
    answer8.place   (x=75,y=155)

def buttfun9(event):
    button9.destroy()
    question9.place (x=20,y=155)
    but9.place      (x=30,y=175)
    answer9.place   (x=50,y=180)

def buttfun10(event):
    button10.destroy()
    question10.place(x=3,y=155)
    but10.place(x=30,y=175)
    answer10.place(x=50,y=180)

button1.bind('<Button>',buttfun1)
button2.bind('<Button>',buttfun2)
button3.bind('<Button>',buttfun3)
button4.bind('<Button>',buttfun4)
button5.bind('<Button>',buttfun5)
button6.bind('<Button>',buttfun6)
button7.bind('<Button>',buttfun7)
button8.bind('<Button>',buttfun8)
button9.bind('<Button>',buttfun9)
button10.bind('<Button>',buttfun10)

but1.bind('<Button>',butans1)
but2.bind('<Button>',butans2)
but3.bind('<Button>',butans3)
but4.bind('<Button>',butans4)
but5.bind('<Button>',butans5)
but6.bind('<Button>',butans6)
but7.bind('<Button>',butans7)
but8.bind('<Button>',butans8)
but9.bind('<Button>',butans9)
but10.bind('<Button>',butans10)

for i in butList:
    i[0].place(y=i[2],x=i[1])

win.mainloop()