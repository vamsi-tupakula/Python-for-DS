import tkinter as tk

my_win = tk.Tk()
my_win.geometry('400x400')

def get_val():
    print(scale.get())

# scale
scale = tk.Scale(my_win,
                 from_=0,
                 to_=100,
                 length=300,
                 orient=tk.HORIZONTAL,
                 font=('Comic Sans', 10),
                 showvalue=0, # hides the current value
                 tickinterval_=10)
scale.set(50) # sets the initial value to 50
scale.pack()

# button to get the value
btn = tk.Button(text='Submit',
                font=('Comic Sans', 12),
                command=get_val)
btn.pack()

my_win.mainloop()