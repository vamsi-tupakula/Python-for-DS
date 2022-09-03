import tkinter as tk

my_win = tk.Tk()
my_win.geometry('400x400')

# basic checkbutton
check_button = tk.Checkbutton(my_win,
                              text='I agree with the privacy policy.',
                              font=('Arial', 10, 'bold'))
check_button.pack()

my_win.mainloop()