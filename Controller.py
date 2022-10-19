from tkinter.filedialog import askopenfilename
from Types.Contact import Contact
from view import MainWindow
import Model
from view import AddContactWindow

def run():
    MainWindow.main_window()


def open_file():
    Model.open_file()


def show_contacts():
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for i in Model.contacts_user:
        i = [i.contact_id, i.name, i.phone, i.comment]
        MainWindow.main_table.insert('', 0, values=i)


def save_contacts():
    pass


def change_contact():
    pass


def delete_contact():
    pass


def search_contact():
    pass


def add_contact(add_entry: list):

    temp = Contact(Model.next_id(), add_entry[0].get(), add_entry[1].get(), add_entry[2].get())
    Model.contacts_user.append(temp)
    AddContactWindow.add_window.destroy()
    show_contacts()
