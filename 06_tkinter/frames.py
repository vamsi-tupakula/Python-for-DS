from tkinter import *

my_win = Tk()
my_win.geometry('400x400')

"""
Frame is a rectangular container to group and hold widgets
"""
frame = Frame(my_win)
frame.pack()

Button(frame,text='W',font=('Consolas', 16), width=3).pack(side=TOP)
Button(frame,text='A',font=('Consolas', 16), width=3).pack(side=LEFT)
Button(frame,text='S',font=('Consolas', 16), width=3).pack(side=LEFT)
Button(frame,text='D',font=('Consolas', 16), width=3).pack(side=LEFT)

# make window non resizable
my_win.resizable(False, False)
my_win.mainloop()