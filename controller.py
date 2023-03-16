import view
import model


def run():
    view.greetings()
    while True:
        view.menu()
        view.decor(20)
        answer = input('Ответ номер: ')
        if answer == '1':
            data = model.read_phonebook()
            view.show_phonebook(data)
        elif answer == '2':
            data = [model.add_contact()]
            view.show_phonebook(data)
            view.print_result('add', data)
        elif answer == '3':
            result = model.find()
            view.show_phonebook(result)
            view.print_result('find', len(result))
        elif answer == '4':
            del_res = model.delete()
            view.show_phonebook(del_res)
            view.print_result('delete', len(del_res))
        elif answer == '5':
            data_up = model.update()
            view.show_phonebook(data_up)
            view.print_result('update', len(data_up))
        elif answer == '6':
            view.print_result('bye', None)
            break
