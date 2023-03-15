spravka = 'phone_book.txt'

def read_phonebook():

    with open(spravka, 'r', encoding='utf8') as book:

        for line in book:

            return line.replace("\r", "").replace("\n", "")

def add_contact(contact):

    with open(spravka, 'a', encoding='utf8') as book:

        book.write('\n' + contact)

    return 'Контакт успешно добавлен в справочник!'

def find(contact):

    with open(spravka, 'r', encoding='utf8') as book:

        count = 0

        for line in book:

            if contact in line:

                count = +1

                return(line.replace("\r", "").replace("\n", ""))

        if count == 0:

            return 'Нет данных, удовлетворяющих введенным значениям!'


def delete_contact(contact):

    with open(spravka, 'r', encoding='utf8') as book:

        lines = book.readlines()

    with open(spravka, 'w', encoding='utf8') as book:

        count = 0

        for line in lines:

            if contact in line:

                count = +1

            else:

                book.write(line)

        if count == 0:

            return False

        else:

            del_number = print("Запись в телефонном справочнике удалена!")

            return(del_number)

def change_contact(name, new_name):

    with open(spravka, 'r', encoding='utf8') as book:

        x = book.read()

    with open(spravka, 'w', encoding='utf8') as book:

        x = x.replace(name, new_name)

        book.write(x)

        change_number = print("Данные изменены")

    return change_number