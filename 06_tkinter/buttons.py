import tkinter as tk

my_win = tk.Tk()
my_win.geometry('400x200')

def my_func():
    print("button clicked...")

# creating basic button
button = tk.Button(my_win,
                   text='Click Me',
                   command=my_func,
                   font=('Comic Sans', 15, 'bold'),
                   bg='#1A4D2E',
                   fg='#FF9F29')
button.pack()

my_win.mainloop()