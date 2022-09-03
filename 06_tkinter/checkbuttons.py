import tkinter as tk

my_win = tk.Tk()
my_win.geometry('400x400')

def display():
    if x.get() == 0:
        print('checkbox is equal to false')
    else:
        print('checkbox is equal to true')

# button variable
x = tk.IntVar()

# basic checkbutton
check_button = tk.Checkbutton(my_win,
                              text='I agree with the privacy policy.',
                              font=('Arial', 10, 'bold'),
                              variable=x,
                              onvalue=1,
                              offvalue=0,
                              command=display)
check_button.pack()

my_win.mainloop()