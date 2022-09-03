from cProfile import label
from tkinter import *

my_win = Tk()
my_win.geometry('400x400')

# title bar
title = Label(text='Enter your Info...',
              font=('Comic Sans', 20, 'bold')).grid(row=0, column=0, columnspan=2)

# first name
f_name_label = Label(my_win,
                     text='First Name : ',
                     font=('Comic Sans', 12)).grid(row=1, column=0)
f_name_entry = Entry(my_win,
                     font=('Comic Sans', 12)).grid(row=1, column=1)

# last name
l_name_label = Label(my_win,
                     text='Last Name : ',
                     width=20,
                     font=('Comic Sans', 12)).grid(row=2, column=0)
l_name_entry = Entry(my_win,
                     font=('Comic Sans', 12)).grid(row=2, column=1)

# email
email_label = Label(my_win,
                     text='Email : ',
                     font=('Comic Sans', 12)).grid(row=3, column=0)
email_entry = Entry(my_win,
                     font=('Comic Sans', 12)).grid(row=3, column=1)

# submit button
submit_btn = Button(my_win,
                    text='Submit',
                    font=('Comic Sans', 13, 'bold')).grid(row=4, column=0, columnspan=2)

my_win.mainloop()