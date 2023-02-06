import csv

def show_menu():
    print("Выберите действие\n"\
            "1. Показать справочник\n"\
            "2. Найти контакт\n"\
            "3. Добавить контакт\n"\
            "4. Удалить запись в тел.книге\n"\
            "5. export_txt\n"\
            "6. exit_prog\n")
    return int(input('Выберите действие '))


def add_new_phonenumber():
    surname = input('Surname: ')
    name = input('Name: ')
    phonenumber = input('Phonenumber: ')
    return [surname, name, phonenumber]


def view_find_phone():
    value = input('Кого ищем? ')
    return value


def delete_value():
    return input('Что удалить? ')