from tkinter import *
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename()
    print(file_path)

my_win = Tk()
my_win.geometry('400x400')

open_btn = Button(text='Choose File',
                  font=('Comic Sans',14),
                  command=select_file)
open_btn.pack()

my_win.resizable(False, False)
my_win.mainloop()