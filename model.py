spravka = 'phone_book.txt'

def read_phonebook():
    with open(spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    return data

def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    with open(spravka, 'a', encoding='utf-8') as file:
        file.write(f'{surname}\t{name}\t{patronymic}\t{phone}\n')

def find():
    query = input('Введите запрос: ')
    with open(spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    results = []
    for contact in data:
        if any(query.lower() in field.lower() for field in contact):
            results.append(contact)
    view.show_phonebook(results)

def delete():
    query = input('Введите запрос: ')
    with open( spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    results = []
    for contact in data:
        if not any(query.lower() in field.lower() for field in contact):
            results.append(contact)
    with open(spravka, 'w', encoding='utf-8') as file:
        for contact in results:
            file.write('\t'.join(contact) + '\n')
    print('Контакты удалены.')

def update():
    query = input('Введите запрос: ')
    field_to_update = input('Введите поле для изменения: ')
    new_value = input('Введите новое значение: ')
    with open(spravka, 'r', encoding='utf-8') as file:
        data = [line.strip().split('\t') for line in file]
    results = []
    for contact in data:
        if query.lower() in contact[0].lower():
            contact[data[0].index(field_to_update)] = new_value
        results.append(contact)
    with open(spravka, 'w', encoding='utf-8') as file:
        for contact in results:
            file.write('\t'.join(contact) + '\n')
    print('Контакты обновлены.')
