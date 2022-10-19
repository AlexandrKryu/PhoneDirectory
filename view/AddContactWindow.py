import tkinter as tk
from functools import partial

from Types import Contact
import Controller
import Model
from Model import contacts_user

add_window: tk.Tk
change_window: tk.Tk
add_entry: [] = []
change_entry: [] = []
temp: Contact.Contact
size_window_add = '310x100+650+350'


def open_window_Add():
    global add_window
    global add_entry

    RESIZEBLE = False

    add_window = tk.Toplevel()
    add_window.title('Создать контакт')
    add_window.geometry(size_window_add)
    add_window.resizable(RESIZEBLE, RESIZEBLE)
    add_window.wm_attributes('-topmost', 1)
    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    name_lable = tk.Label(add_window, text='Имя')
    phone_lable = tk.Label(add_window, text='Телефон')
    comment_lable = tk.Label(add_window, text='Коментарий')
    name_lable.grid(column=0, row=0, stick='e')
    phone_lable.grid(column=0, row=1, stick='e')
    comment_lable.grid(column=0, row=2, stick='e')

    add_entry = [tk.Entry(add_window, width=30) for _ in range(3)]
    for i, entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)

    add_button = tk.Button(add_window, text='Создать', command=partial(Controller.add_contact, add_entry))
    add_button.grid(column=1, row=3)

    add_window.mainloop()



