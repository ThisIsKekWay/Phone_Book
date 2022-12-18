from vvod import writing_phone_book
from search import searching
from export import export_contacts


def validation(lst):
    val_name = False
    val_num = False
    for i in range(len(lst)):
        if i == 0:
            for j in lst[i]:
                if j not in '1234567890+-*/.,<>`~!@#$%^&*()_|':
                    val_name = True
                else:
                    val_name = False
                    break
            if val_name:
                print('Проверка имени пройдена')
            else:
                print('Провекра имени не пройдена, в имени могут быть только буквы')
        elif i == 1:
            try:
                int(lst[i])
                val_num = True
                print('Проверка номера пройдена')
            except:
                val_num = False
                print('Провекра номера не пройдена, в номере могут быть только цифры')
        else:
            break
    res = val_num and val_name
    return res


def take_note():
    a = 1
    while a != 0:
        input_data = input('Введите через пробел: Фамилия, Номер телефона, Комментарий\n').split(' ', 2)
        if input_data[0] == '1':
            break
        if validation(input_data):
            str1 = '; '.join(input_data)
            writing_phone_book(str1)
        print('Когда достаточно: введите "1"')


def choose_mode():
    mode = input('Выберите режим работы\n'
                 '1) Режим внесения записей\n'
                 '2) Режим просмотра записей\n'
                 '3) Режим поиска по фамилии\n')

    if mode == '1':
        print('Выбран режим внесения записей\n')
        take_note()
    elif mode == '2':
        data = 'book.csv'
        mode1 = input('Выбран режим просмотра записей\n'
                      'Выберите вид записей:\n'
                      '1) Показать записи одной строкой\n'
                      '2) Показать записи "в столбик\n')
        if mode1 == '1':
            sepa = ' '
            export_contacts(data, sepa)
        elif mode1 == '2':
            sepa = '\n'
            export_contacts(data, sepa)
    elif mode == '3':
        print('Выбран режим поиска по фамилии')
        name = input('Введите фамилию для поиска\n').split()
        searching(name[0])
        data = 'results.csv'
        mode1 = input('Выбран режим просмотра записей\n'
                      'Выберите вид записей:\n'
                      '1) Показать записи одной строкой\n'
                      '2) Показать записи "в столбик\n')
        if mode1 == '1':
            sepa = ' '
            export_contacts(data, sepa)
        elif mode1 == '2':
            sepa = '\n'
            export_contacts(data, sepa)

    else:
        print('Выбранный режим не распознан')


choose_mode()
