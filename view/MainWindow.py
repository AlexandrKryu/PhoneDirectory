from functools import partial
from turtle import width
import Controller
import tkinter as tk
from tkinter import Frame, ttk
from view import AddContactWindow, ChangeContactWindow, Geometry

size_window = '630x420+500+250'
main_table: ttk.Treeview
contact_list = []

def get_contact(event):
    global contact_list
    items = main_table.selection()[0]
    contact_list = [i for i in main_table.item(items, option="values")]


def main_window():
    global contact_list
    first_window = tk.Tk()
    first_window.title('Телефонный справочник')
    first_window.geometry(size_window)
    first_window.wm_attributes('-topmost', 1)
    first_window.focus_set()

    button_show = tk.Button(text = 'Показать контакты', command= Controller.show_contacts)
    button_show.grid(column=0, row=1, stick='ew')
    button_open_file = tk.Button(text = 'Открыть файл', width=20, command=Controller.open_file)
    button_open_file.grid(column=0, row=2, stick='s')
    button_save_file = tk.Button(text = 'Сохранить файл', width=20)
    button_save_file.grid(column=0, row=3, stick='s')
    button_add_contact = tk.Button(text = 'Добавить контакт', width=20, command=AddContactWindow.open_window_Add)
    button_add_contact.grid(column=0, row=4, stick='s')
    button_change_contact = tk.Button(text = 'Изменить контакт', width=20, command=ChangeContactWindow.open_window)
    button_change_contact.grid(column=0, row=5, stick='s')
    button_delete_contact = tk.Button(text = 'Удалить контакт', width=20)
    button_delete_contact.grid(column=0, row=6, stick='s')
    lable = tk.Label(text = 'Введите имя:')
    lable.place(x = 2, y = 180)
    entry = tk.Entry(width=25)
    entry.place(x = 2, y = 200)
    button_search_contact = tk.Button(text = 'Поиск', width=20)
    button_search_contact.place(x = 2, y = 220)

    frame = Frame(first_window, width=100)
    frame.place(x = 150, y = 0)
    global main_table
    main_table = ttk.Treeview(frame, show='headings', height=20)
    heads = ['id', 'Имя', 'Телефон', 'Комментарий']
    main_table['columns'] = heads
    main_table.column('id', width=30)
    for header in heads:
        main_table.heading(header, text=header, anchor='w')
        if header != 'id':
            main_table.column(header, width=150)
    main_table.pack()
    main_table.bind("<<TreeviewSelect>>", get_contact)

    tk.mainloop()