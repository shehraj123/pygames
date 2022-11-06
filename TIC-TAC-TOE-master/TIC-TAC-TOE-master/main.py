import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import itertools

i = 0
w={}

#Other Functions
def i_reset():
    global i
    i=0

def w_reset():
    global w
    w={}

def c_checker():
    if i%2==0:
        return "X"
    else:
        return "O"

c = c_checker()
root = Tk()

title = Label(root, text="TIC-TAC-TOE").grid(row=0, column=1)

def win_check():

    global w
    x_pos=()
    o_pos=()
    x_sub=()
    o_sub=()
    w_pos=((1,4,7),(2,5,8),(3,6,9),(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7))

    for x in range(1,10):
        try:
            if w[x]=='X':
                x_pos=list(x_pos)
                x_pos.append(x)
                x_pos=tuple(x_pos)

            if w[x]=='O':
                o_pos=list(o_pos)
                o_pos.append(x)
                o_pos=tuple(o_pos)

        except KeyError:
            continue

    x_sub = set(itertools.combinations(x_pos,3))
    o_sub = set(itertools.combinations(o_pos,3))

    a = False

    for e in x_sub:
        if e in w_pos:
            messagebox.showinfo("Game Ended","X Wins!!")
            a = True
            i_reset()
    for e in o_sub:
        if e in w_pos:
            messagebox.showinfo("Game Ended","O Wins!!")
            a = True
            i_reset()

    if a == False and i==9 :
        messagebox.showinfo("Game Ended","It is a Draw!!")
        i_reset()

#Button_Functions
def button1():
    if Button1['text']=='X' or Button1['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[1]=c
        Button1['text']=c
        global i
        i+=1
        win_check()


def button2():
    if Button2['text']=='X' or Button2['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[2]=c
        Button2['text']=c
        global i
        i+=1
        win_check()


def button3():
    if Button3['text']=='X' or Button3['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[3]=c
        Button3['text']=c
        global i
        i+=1
        win_check()


def button4():
    if Button4['text']=='X' or Button4['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[4]=c
        Button4['text']=c
        global i
        i+=1
        win_check()

def button5():
    if Button5['text']=='X' or Button5['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[5]=c
        Button5['text']=c
        global i
        i+=1
        win_check()

def button6():
    if Button6['text']=='X' or Button6['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[6]=c
        Button6['text']=c
        global i
        i+=1
        win_check()

def button7():
    if Button7['text']=='X' or Button7['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[7]=c
        Button7['text']=c
        global i
        i+=1
        win_check()

def button8():
    if Button8['text']=='X' or Button8['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[8]=c
        Button8['text']=c
        global i
        i+=1
        win_check()

def button9():
    if Button9['text']=='X' or Button9['text']=='O':
        pass
    else:
        c = c_checker()
        global w
        w[9]=c
        Button9['text']=c
        global i
        i+=1
        win_check()

def reset():
    button_disabler()
    i_reset()
    w_reset()



def button_disabler():
    Button1['text']=''
    Button2['text']=''
    Button3['text']=''
    Button4['text']=''
    Button5['text']=''
    Button6['text']=''
    Button7['text']=''
    Button8['text']=''
    Button9['text']=''





#Buttons
Button1 = Button(root,command = button1,height=5,width=10)
Button1.grid(row=1,column=0)
Button2 = Button(root, command = button2,height=5,width=10)
Button2.grid(row=1,column=1)
Button3 = Button(root, command = button3,height=5,width=10)
Button3.grid(row=1,column=2)
Button4 = Button(root, command = button4,height=5,width=10)
Button4.grid(row=2,column=0)
Button5 = Button(root, command = button5,height=5,width=10)
Button5.grid(row=2,column=1)
Button6 = Button(root, command = button6,height=5,width=10)
Button6.grid(row=2,column=2)
Button7 = Button(root, command = button7,height=5,width=10)
Button7.grid(row=3,column=0)
Button8 = Button(root, command = button8,height=5,width=10)
Button8.grid(row=3,column=1)
Button9 = Button(root, command = button9,height=5,width=10)
Button9.grid(row=3,column=2)
Reset = Button(root,text='Reset', command = reset)
Reset.grid(row=4,column=1)

root.mainloop()
