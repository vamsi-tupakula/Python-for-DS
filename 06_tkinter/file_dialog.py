from tkinter import *
from tkinter import filedialog

def select_file():
    # set initial dir path to open
    file_path = filedialog.askopenfilename(initialdir='C:\\Users\\HP\\OneDrive\\Pictures',
                                           title='Please choose a file..',
                                           filetypes=(('text files', '*.txt'),('python files','*.py')))
    print(file_path)

my_win = Tk()
my_win.geometry('400x400')

open_btn = Button(text='Choose File',
                  font=('Comic Sans',14),
                  command=select_file)
open_btn.pack()

my_win.resizable(False, False)
my_win.mainloop()