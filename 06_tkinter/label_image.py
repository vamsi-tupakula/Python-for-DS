import tkinter as tk

my_win = tk.Tk()
my_win.geometry('400x400')

photo = tk.PhotoImage(file='icon.png')

label = tk.Label(my_win, text='Hey! Tkinter..', font=('Arial', 20, 'bold'), fg='#1572A1', bg='#EFDAD7', padx=10, pady=5,image=photo, compound='top')
label.pack() 

my_win.mainloop()