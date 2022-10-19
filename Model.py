from tkinter.filedialog import askopenfilename

import Types.Contact
from Types.Contact import Contact

contacts_user: list = []
max_id = '0'


def open_file():
    global max_id
    types = (("all files", "*.*"),)
    file_name = askopenfilename(title='Открыть базу данных', filetypes=types)
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            user_list = line.replace('\n', '').split(';')
            user = Contact(user_list[0], user_list[1], user_list[2], user_list[3])
            if int(max_id) <= int(user_list[0]):
                max_id = str(int(user_list[0]))
            contacts_user.append(user)

def next_id():
    global max_id
    max_id = str(int(max_id) + 1)
    return max_id
