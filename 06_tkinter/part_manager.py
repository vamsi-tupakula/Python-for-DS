from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

# functions
def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please Include all fields..')
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    populate_list()

def select_item(event):
    print('select')

def remove_item():
    print('remove')

def update_item():
    print('update')

def clear_text():
    print('clear')

my_win = Tk()
my_win.title('Part Manager')
my_win.geometry('700x350')

# part
part_text = StringVar()
part_label = Label(my_win, text="Part Name", font=('bold', 14), pady=20, padx=10)
part_label.grid(row=0, column=0,sticky=W)
part_entry = Entry(my_win, textvariable=part_text,font=('bold', 14))
part_entry.grid(row=0, column=1)

# customer
customer_text = StringVar()
customer_label = Label(my_win, text="Customer", font=('bold', 14), padx=10)
customer_label.grid(row=0, column=2,sticky=W)
customer_entry = Entry(my_win, textvariable=customer_text,font=('bold', 14))
customer_entry.grid(row=0, column=3)

# retailer
retailer_text = StringVar()
retailer_label = Label(my_win, text="Retailer", font=('bold', 14), padx=10)
retailer_label.grid(row=1, column=0,sticky=W)
retailer_entry = Entry(my_win, textvariable=retailer_text,font=('bold', 14))
retailer_entry.grid(row=1, column=1)

# price
price_text = StringVar()
price_label = Label(my_win, text="Price", font=('bold', 14), padx=10)
price_label.grid(row=1, column=2,sticky=W)
price_entry = Entry(my_win, textvariable=price_text,font=('bold', 14))
price_entry.grid(row=1, column=3)

# Parts List (ListBox)
parts_list = Listbox(my_win, width=60, height=8, border=0, font=('Arial',10,'bold'))
parts_list.grid(row=3, column=0 , columnspan=3, rowspan=6, padx=20, pady=20)

# create scrollbar
scrollbar = Scrollbar(my_win)
scrollbar.grid(row=3,column=3)

# linking scrollbar to parts_list
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# binding select
parts_list.bind('<<ListboxSelect>>', select_item)

# buttons
add_btn = Button(my_win,text='Add Part', font=('bold', 10), width=12,  command=add_item)
add_btn.grid(row=2,column=0, pady=20, padx=15)

remove_btn = Button(my_win,text='Remove Part', font=('bold', 10), width=12,  command=remove_item)
remove_btn.grid(row=2,column=1, padx=15)

update_btn = Button(my_win,text='Update Part', font=('bold', 10), width=12,  command=update_item)
update_btn.grid(row=2,column=2, padx=15)

clear_btn = Button(my_win,text='Clear Input', font=('bold', 10), width=12,  command=clear_text)
clear_btn.grid(row=2,column=3, padx=15)

# populate data
populate_list()

my_win.resizable(False, False)
my_win.mainloop()