from tkinter import *

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
parts_list = Listbox(my_win, width=60, height=8, border=0)
parts_list.grid(row=3, column=0 , columnspan=3, rowspan=6, padx=20, pady=20)

# create scrollbar
scrollbar = Scrollbar(my_win)
scrollbar.grid(row=3,column=3)

# linking scrollbar to parts_list
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

my_win.resizable(False, False)
my_win.mainloop()