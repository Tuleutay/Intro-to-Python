import view as v
import model as m


def start():
    key = v.show_menu()
    data = m.get_data('phonebook.csv')
    if key == 6:
        print()
    else:
        if key == 1:
            print(data)
            print()
        elif key == 2:
            print(m.find_phone(data, v.view_find_phone()))
            print()
        elif key == 3:
            m.new_phonenumber(data, v.add_new_phonenumber())
            m.save_data('phonebook.csv', data)
            print()
        elif key == 4:
            print(m.delete_phonenumber(data,v.delete_value()))
            m.save_data('phonebook.csv', data)
            print()
        elif key == 5:
            m.export_txt('text_members.txt', data)
            print()
        start()



# def del_member():
#     return m.delete_phonenumber(v.view_delet())
#
# def export_json():
#     # peredat'slovar'
#     return 0





