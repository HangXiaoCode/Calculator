from tkinter import *
master = Tk()

display = 0

t1 = 0

process = 0

result = 0

def callback1():
    global display
    display = display * 10 + 1
    T.delete('1.0', END)
    T.insert(END, display)

def callback2():
    global display
    display = display * 10 + 2
    T.delete('1.0', END)
    T.insert(END, display)

def callback3():
    global display
    display = display * 10 + 3
    T.delete('1.0', END)
    T.insert(END, display)

def callback4():
    global display
    display = display * 10 + 4
    T.delete('1.0', END)
    T.insert(END, display)

def callback5():
    global display
    display = display * 10 + 5
    T.delete('1.0', END)
    T.insert(END, display)

def callback6():
    global display
    display = display * 10 + 6
    T.delete('1.0', END)
    T.insert(END, display)

def callback7():
    global display
    display = display * 10 + 7
    T.delete('1.0', END)
    T.insert(END, display)

def callback8():
    global display
    display = display * 10 + 8
    T.delete('1.0', END)
    T.insert(END, display)

def callback9():
    global display
    display = display * 10 + 9
    T.delete('1.0', END)
    T.insert(END, display)

def callback0():
    global display
    display = display * 10 + 0
    T.delete('1.0', END)
    T.insert(END, display)

def callbackplus():
    global display
    global t1
    global process
    t1=display
    if process != 0:
        sys.exit("errors!")
    print(t1)
    display = 0
    process = 1
    T.delete('1.0', END)
    T.insert(END, '+')

def callbackminus():
    global display
    global t1
    global process
    t1=display
    if process != 0:
        sys.exit("errors!")
    print(t1)
    display = 0
    process = 2
    T.delete('1.0', END)
    T.insert(END, '-')

def callbacktimes():
    global display
    global t1
    global process
    t1 = display
    if process != 0:
        sys.exit("errors!")
    print(t1)
    display = 0
    process = 3
    T.delete('1.0', END)
    T.insert(END, '*')

def callbackdivide():
    global display
    global t1
    global process
    t1 = display
    if process != 0:
        sys.exit("errors!")
    print(t1)
    display = 0
    process = 4
    T.delete('1.0', END)
    T.insert(END, '/')

def callbackequal():
    global display
    global t1
    global process
    global result
    t2 = display
    print(t2)
    if process == 1:
        result = t1 + t2
    elif process == 2:
        result = t1 - t2
    elif process == 3:
        result = t1 * t2
    else:
        result = t1 / t2
    display=result
    process = 0
    T.delete('1.0', END)
    T.insert(END, display)

def callbackclear():
    global display
    display = 0
    T.delete('1.0', END)
    T.insert(END, display)


MyButton1 = Button(master, text="1", width=10, command=callback1)
MyButton1.grid(row=0, column=0)

MyButton2 = Button(master, text="4", width=10, command=callback4)
MyButton2.grid(row=1, column=0)

MyButton3 = Button(master, text="7", width=10, command=callback7)
MyButton3.grid(row=2, column=0)

MyButton4 = Button(master, text="2", width=10, command=callback2)
MyButton4.grid(row=0, column=1)

MyButton5 = Button(master, text="5", width=10, command=callback5)
MyButton5.grid(row=1, column=1)

MyButton6 = Button(master, text="8", width=10, command=callback8)
MyButton6.grid(row=2, column=1)

MyButton7 = Button(master, text="3", width=10, command=callback3)
MyButton7.grid(row=0, column=2)

MyButton8 = Button(master, text="6", width=10, command=callback6)
MyButton8.grid(row=1, column=2)

MyButton9 = Button(master, text="9", width=10, command=callback9)
MyButton9.grid(row=2, column=2)

MyButton0 = Button(master, text="0", width=10, command=callback0)
MyButton0.grid(row=3, column=1)

MyButtonplus = Button(master, text="+", width=10, command=callbackplus)
MyButtonplus.grid(row=3, column=0)

MyButtonminus = Button(master, text="-", width=10, command=callbackminus)
MyButtonminus.grid(row=3, column=2)

MyButtontimes = Button(master, text="*", width=10, command=callbacktimes)
MyButtontimes.grid(row=4, column=0)

MyButtondivide = Button(master, text="/", width=10, command=callbackdivide)
MyButtondivide.grid(row=4, column=1)

MyButtonequal = Button(master, text="=", width=10, command=callbackequal)
MyButtonequal.grid(row=4, column=2)

MyButtonCE = Button(master, text='C', width=10, command=callbackclear)
MyButtonCE.grid(row=5, column=0)

T = Text(master, width = 30)
T.grid(row=6, column=0, columnspan = 3)


mainloop()
