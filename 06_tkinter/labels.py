import tkinter as tk

"""
What is a widget?
widgets are any GUI elements like buttons, labels, images etc...
What is a window?
window in tkinter serves as a container to hold these widgets
What is a label?
An area widget that holds text and/or image within a window
"""

my_win = tk.Tk()
my_win.geometry('400x400')

# creating a basic label
label = tk.Label(my_win, text='Hey! Label')
label.pack() # this will by default places the label at top-center

my_win.mainloop()