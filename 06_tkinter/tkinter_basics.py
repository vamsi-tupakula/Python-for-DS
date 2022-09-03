import tkinter as tk

# create basic window
my_win = tk.Tk() # instantiate an instance of window

# change the geometry of window
my_win.geometry('400x400')

# change the window title
my_win.title('GUI using Tkinter')

# change the icon of the window
icon = tk.PhotoImage(file='icon.png')
my_win.iconphoto(True, icon)

# make changes to the window
my_win.config(bg='#ECE5C7')

my_win.mainloop()