import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

frame = tk.Tk()
frame.geometry('300x300')
frame.title("Falcon's Notepad")

saved = tk.BooleanVar()
saved.set(True)

def key_pressed(event):
    saved.set(False)

def on_close():
    print(saved)
    if saved.get() == False:
        if messagebox.askyesno('', 'Do you want to save the changes?') == True:
            if save_as_click() == True:
                frame.destroy()
        else:
            frame.destroy()

    else:
        frame.destroy()

def change_title(fn):
    items = fn.split('/')
    frame.title('Falconpad - ' + items[len(items) - 1])
    

def open_click():
    file_name = filedialog.askopenfilename()

    if len(file_name) >0:
        # saved.set( True)
        fobj = open(file_name, 'r')
        data = fobj.read()
        fobj.close()
        text.delete('1.0', tk.END)
        text.insert(tk.END, data)
        change_title(file_name)
        file_menu.entryconfig(3, state = tk.NORMAL)


def save_as_click():
    file_name = filedialog.asksaveasfilename()

    if len(file_name) > 0:
        data = text.get('1.0', tk.END)
        fobj = open(file_name, 'w')
        fobj.write(data)
        change_title(file_name)
        saved.set(True)
        file_menu.entryconfig(3, state = tk.NORMAL)
        return saved

def save_click():
    file_name = save_as_click()
    fobj = open(file_name, 'w')
    data = text.get('1.0', tk.END)
    fobj.write(data)

def new_click():
    if saved.get() == False:
        save_as_click()
    text.delete('1.0', tk.END)
    change_title('')


def copy_click():
    # global data
    # if text.selection_get():
    #     data = text.selection_get()

    text.event_generate('<<Copy>>')

def paste_click():
    # global data
    # text.insert(tk.END, data)
    text.event_generate('<<Paste>>')

def cut_click():
    # global data
    # if text.selection_get():
    #     data= text.selection_get()
    #     text.delete('sel.first', 'sel.last')
    text.event_generate('<<Cut>>')


bar = tk.Menu()
frame.config(menu=bar)

file_menu = tk.Menu()
file_menu.add_command(label = 'New', command=new_click)
file_menu.add_command(label = 'Open', command=open_click)
file_menu.add_command(label = 'Save as', command=save_as_click)
save = file_menu.add_command(label = 'Save', command= save_click, state=tk.DISABLED)
file_menu.add_separator()
file_menu.add_command(label = 'Exit')

edit_menu = tk.Menu()
edit_menu.add_command(label = 'Copy', command=copy_click)
edit_menu.add_command(label = 'Paste', command=paste_click)
edit_menu.add_command(label = 'Cut', command=cut_click)

bar.add_cascade(label = 'File', menu= file_menu)
bar.add_cascade(label = 'Edit', menu = edit_menu)


scrl1 = tk.Scrollbar(frame)
scrl1.pack(side=tk.RIGHT, fill=tk.Y)


text = tk.Text(frame, yscrollcommand=scrl1.set)
text.pack()

text.bind_all('<KeyPress>', key_pressed)
# text.bind('<Selection>', select_text)

scrl1.config(command=text.yview)

frame.protocol('WM_DELETE_WINDOW', on_close)

print(saved)
frame.mainloop()