def greetings():
    decor(20)
    print('Добро пожаловать в телефонный справочник!')
    decor(20)


def menu():
    print('Выберите действие:\n'
          '\t\t1. Показать все контакты\n'
          '\t\t2. Добавить новый контакт\n'
          '\t\t3. Найти контакт\n'
          '\t\t4. Удалить контакт\n'
          '\t\t5. Изменить контакт\n'
          '\t\t6. Выйти из программы')


def show_phonebook(data):
    if not data:
        decor(20)
        print('Справочник пуст')
        decor(20)
    else:
        decor(80)
        print('{:<5} {:<20} {:<20} {:<20} {:<20}'.format('№', 'Фамилия', 'Имя', 'Отчество', 'Телефон'))
        decor(80)
        for i, contact in enumerate(data):
            print('{:<5} {:<20} {:<20} {:<20} {:<20}'.format(i+1, *contact))
        decor(20)

def decor(x):
    print('-' * x)

def print_result(operation, count):
    if operation == 'find':
        if count == 0:
            print('Контактов не найдено')
        elif count == 1:
            print(f'Найден {count} контакт')
        elif 2 <= count <= 4:
            print(f'Найдено {count} контакта')
        else:
            print(f'Найдено {count} контактов')
    elif operation == 'add':
        for i in count:
            if '-' in i:
                print('Контакт не добавлен')
            else:
                print('Контакт добавлен')
    elif operation == 'delete':
        if count == 0:
            print('Контакты не были удалены')
        elif count == 1:
            print(f'{count} Контакт был удален')
        elif 2 <= count <= 4:
            print(f'{count} Контакта было удалено')
        else:
            print(f'{count} Контактов было удалено')
    elif operation == 'update':
        if count == 0:
            print('Контакты не были изменены')
        elif count == 1:
            print(f'{count} Контакт был изменен')
        elif 2 <= count <= 4:
            print(f'{count} Контакта было изменено')
        else:
            print(f'{count} Контактов было изменено')
    elif operation == 'bye':
        decor(20)
        print('Всего хорошего!')

    decor(20)