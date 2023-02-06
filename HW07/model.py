import csv


def get_data(file_name):
    data = []
    with open(file_name, 'r', encoding='utf8') as file:
        for row in file:
            data.append([row.strip("\n")])
    return data

def save_data(file_name,data):
    with open(file_name, 'w', encoding='utf8') as f:
        for row in data:
            for i in row:
                lst = i.split(';')
                f.write(f'{lst[0]};{lst[1]};{lst[2]}\n')

def new_phonenumber(data,add):
    data.append([f'{add[0]};{add[1]};{add[2]};'])
    print('Add new phonenumber')



def find_phone(book, key):
    for row in book:
        for j in row:
            if key in j:
                return j
    return 'Not found value'


def delete_phonenumber(book, key):
    for i in book:
        for j in i:
            if key in j:

                book.pop(book.index(i))
                return 'phonenumber deleted'
    return 'Not found value'


def export_txt(file_name,data):
    with open(file_name,'w', encoding='utf8') as txt_file:
        for row in data:
            for i in row:
                lst = i.split(';')
                txt_file.write(f'{lst[0]};{lst[1]};{lst[2]}\n')
        print(f'Данные записаны в файле {file_name}')

