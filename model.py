spravka = 'phone_book.txt'


def read_phonebook():
    with open(spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    return data


def add_contact():
    surname = input('Введите фамилию: ').strip()
    name = input('Введите имя: ').strip()
    patronymic = input('Введите отчество: ').strip()
    phone = input('Введите номер телефона: ').strip()
    with open(spravka, 'a', encoding='utf-8') as file:
        if surname and name and patronymic and phone:
            file.write(f'{surname}\t{name}\t{patronymic}\t{phone}\n')

    return surname or "-", name or "-", patronymic or "-", phone or "-"


def find():
    query = input('Введите запрос: ')
    with open(spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    results = []
    for contact in data:
        if any(query.lower() in field.lower() for field in contact):
            results.append(contact)

    return results


def delete():
    query = input('Введите запрос: ')
    with open(spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    results = []
    del_res = []
    for contact in data:
        if not any(query.lower() in field.lower() for field in contact):
            results.append(contact)
        else:
            del_res.append(contact)
    with open(spravka, 'w', encoding='utf-8') as file:
        for contact in results:
            file.write('\t'.join(contact) + '\n')
    return del_res


def update():
    query = input('Введите контакт, который хотите изменить: ')
    field_to_update = int(input('Введите, число:\n'
                                '1. Изменить Фамилию\n'
                                '2. Изменить Имя\n'
                                '3. Изменить Отчество\n'
                                '4. Изменить Телефон\n'))
    new_value = input('Введите новое значение: ')
    with open(spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    updated_data = []
    update_line = []
    for contact in data:
        if any(query.lower() in field.lower() for field in contact):
            contact[field_to_update - 1] = new_value
            update_line.append(contact)
        updated_data.append(contact)
    with open(spravka, 'w', encoding='utf-8') as file:
        for contact in updated_data:
            file.write('\t'.join(contact) + '\n')
    return update_line
