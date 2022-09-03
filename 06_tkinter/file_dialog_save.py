from tkinter import *
from tkinter import filedialog

my_win = Tk()

def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('text file', '.txt'),('HTML file', '.html'), ('All files', '.*')])
    text_content = str(text.get(1.0, END))
    file.write(text_content)
    file.close()

# text area to add some text
text = Text(my_win,
            font=('Lucida Sans Typewriter', 22),
            wrap=WORD,
            height=8,
            width=22,
            padx=5,
            pady=10)
text.pack()

save_btn = Button(text='Save',
                  font=('Consolas', 14, 'bold'),
                  command=save_file)
save_btn.pack()

my_win.resizable(False, False)
my_win.mainloop()