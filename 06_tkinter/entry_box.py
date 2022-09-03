import tkinter as tk

my_win = tk.Tk()
my_win.geometry('500x100')

# submit function
def submit():
    entry_text = entry.get()
    print(entry_text)
    # disable entry box after first submit
    entry.config(state=tk.DISABLED)

# delete function
def delete():
    entry.delete(0,tk.END)

# backspace function
def backspace():
    entry.delete(len(entry.get())-1,tk.END)

# create basic entrybox
entry = tk.Entry(my_win,
                 font=('Comic Sans', 18))
entry.insert(0, "Name is :") # similar to placeholder..
entry.pack(side='left')

# create submit button
submit_btn = tk.Button(my_win,
                       text='Submit',
                       font=('Comic Sans', 13, 'bold'),
                       command=submit)
submit_btn.pack(side='right')

# create delete button
delete_btn = tk.Button(my_win,
                       text='Delete',
                       font=('Comic Sans', 13, 'bold'),
                       command=delete)
delete_btn.pack(side='right')

# create backspace button
backspace_btn = tk.Button(my_win,
                       text='backspace',
                       font=('Comic Sans', 13, 'bold'),
                       command=backspace)
backspace_btn.pack(side='right')

my_win.mainloop()