import shutil


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Изменить данные абонента в справочнике\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Номер", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 8):
        if choice == 1:
            show_phonebook(phone_book)
        elif choice == 2:
            show_phonebook(find_by_surname(phone_book))
        elif choice == 3:
            show_phonebook(find_by_number(phone_book))
        elif choice == 4:
            add_user(phone_book)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            delete_user(phone_book)
            rewrite_csv('phonebook.csv', phone_book)
        elif choice == 6:
            change_user_data(phone_book)
            rewrite_csv('phonebook.csv', phone_book)
        elif choice == 7:
            turn_to_text()
        choice = show_menu()

# 1


def show_phonebook(phone_book):
    for elem in phone_book:
        for key in elem:
            print(f'{key} : {elem[key]}')
        print()

# 2


def find_by_surname(phone_book):
    surname = input("Введите фамилию: ")
    results = []
    for elem in phone_book:
        if elem['Фамилия'] == surname:
            results.append(elem)
    return results

# 3


def find_by_number(phone_book):
    number = input("Введите номер телефона: ")
    results = []
    for elem in phone_book:
        if elem['Номер'] == number:
            results.append(elem)
    return results

# 4


def add_user(phone_book):
    record = dict()
    for k in phone_book[0].keys():
        record[k] = input(f"Введите {k}: ")
    phone_book.append(record)


def write_csv(filename, phone_book):
    with open(filename, 'a', encoding='utf-8') as data:
        line = ''
        for v in phone_book[-1].values():
            line += v + ', '
        data.write(f"{line[:-1]}\n")


# 5

def delete_user(phone_book):
    deleted_user = input("Введите фамилию человека, которого нужно удалить: ")
    for elem in phone_book:
        for v in elem.values():
            if v == deleted_user:
                phone_book.remove(elem)


def rewrite_csv(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as data:
        for i in range(len(phone_book)):
            line = ''
            for v in phone_book[i].values():
                line += v + ', '
            data.write(f"{line[:-1]}\n")

# 6


def change_user_data(phone_book):
    user = input("Введите фамилию абонента, которого нужно изменить: ")
    old_attr = input("Введите наименования поля для изменения: ")
    new_attr = input("Введите новое значение для поля: ")
    for elem in phone_book:
        for v in elem.values():
            if v == user:
                elem[old_attr] = elem[old_attr].replace(
                    elem[old_attr], new_attr)

# 7


def turn_to_text():
    filename = input("Введите имя файла для сохранения: ")
    shutil.copyfile('phonebook.csv', f'{filename}.txt')


work_with_phonebook()
