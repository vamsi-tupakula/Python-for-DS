import tkinter as tk

my_win = tk.Tk()
my_win.geometry('400x200')

# submit function
def submit():
    entry_text = entry.get()
    print(entry_text)

# create basic entrybox
entry = tk.Entry(my_win,
                 font=('Comic Sans', 14))
entry.pack()

# create submit button
submit_btn = tk.Button(my_win,
                       text='Submit',
                       font=('Comic Sans', 13, 'bold'),
                       command=submit)
submit_btn.pack()

my_win.mainloop()