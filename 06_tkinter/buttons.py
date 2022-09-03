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
                   fg='#FF9F29',
                   activeforeground='#FF9F29',
                   activebackground='#1A4D2E',
                   # state=tk.DISABLED
                   )
button.pack()

my_win.mainloop()