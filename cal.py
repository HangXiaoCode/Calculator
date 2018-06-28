from tkinter import *
master = Tk()

display = 0

def callback():
    global display
    display = display * 10 + 1
    T.delete('1.0', END)
    T.insert(END, display)

MyButton1 = Button(master, text="1", width=10, command=callback)
MyButton1.grid(row=0, column=0)

MyButton2 = Button(master, text="4", width=10, command=callback)
MyButton2.grid(row=1, column=0)

MyButton3 = Button(master, text="7", width=10, command=callback)
MyButton3.grid(row=2, column=0)

MyButton4 = Button(master, text="2", width=10, command=callback)
MyButton4.grid(row=0, column=1)

MyButton5 = Button(master, text="5", width=10, command=callback)
MyButton5.grid(row=1, column=1)

MyButton6 = Button(master, text="8", width=10, command=callback)
MyButton6.grid(row=2, column=1)

MyButton7 = Button(master, text="3", width=10, command=callback)
MyButton7.grid(row=0, column=2)

MyButton8 = Button(master, text="6", width=10, command=callback)
MyButton8.grid(row=1, column=2)

MyButton9 = Button(master, text="9", width=10, command=callback)
MyButton9.grid(row=2, column=2)

T = Text(master, width = 30)
T.grid(row=3, column=0, columnspan = 3)
#T.grid(row=3, column=0)


mainloop()
