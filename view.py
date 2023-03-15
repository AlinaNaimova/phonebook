def greetings():
    print('Приветствую! Выберите пункт, который вас интересует.')

def menu():
    print('Выберите действие:\n'
          '1. Показать все контакты\n'
          '2. Добавить новый контакт\n'
          '3. Найти контакт\n'
          '4. Удалить контакт\n'
          '5. Изменить контакт\n'
          '6. Выйти из программы')


def show_phonebook(contacts):
    if len(contacts) == 0:
        print("Телефонный справочник пуст!")
    else:
        for contact in contacts:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")