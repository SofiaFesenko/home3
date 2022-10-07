from collections import UserDict


class AddressBook(UserDict):
    def has_in_keys(self, key):
        return key in self.data.keys()


class Field():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @staticmethod
    def add():
        name = input('input name')
        address_dict[phone] = name
        print(address_dict)

    @staticmethod
    def update():
        new_name = input('input new name')
        address_dict[phone] = new_name
        print(address_dict)

    @staticmethod
    def destroy():
        del address_dict[phone]
        print(address_dict)


class Record(Field):
    @staticmethod
    def add():
        name = input('input name')
        address_dict[phone] = name
        print(address_dict)

    @staticmethod
    def update():
        new_name = input('input new name')
        address_dict[phone] = new_name
        print(address_dict)

    @staticmethod
    def destroy():
        del address_dict[phone]
        print(address_dict)


address_dict = AddressBook()
while True:
    phone = input('input phone number or break(if you want to exit)')
    if phone != 'break':
        if phone in address_dict.keys():
            ans = input('you already have this number. do you want to update it or delete? (u/d)')
            if ans == 'u':
                Record.update()
            else:
                Record.destroy()
        else:
            print('you don`t have this number')
            Record.add()
    else:
        break

