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
my_win.geometry('600x600')

# create photoimage
photo = tk.PhotoImage(file='photo.png')

# creating a basic label
label = tk.Label(my_win, text='Hey! Label', font=('Arial', 20, 'bold'), fg='#1572A1', bg='#EFDAD7', padx=10, pady=5,image=photo, compound='bottom')
label.pack() # this will by default places the label at top-center
# label.place(x=10, y=10) # this places label at certain coordinates

my_win.mainloop()