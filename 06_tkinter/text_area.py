from tkinter import *

my_win = Tk()

def submit():
    print(text.get('1.0', END))

# text area
text = Text(my_win,
            font=('Ink Free', 25),
            height=8,
            width=20,
            padx=5,
            pady=10)
text.pack()

button = Button(text='Done',
                font=('Consolas', 13, 'bold'),
                command=submit).pack()

my_win.resizable(False, False)
my_win.mainloop()