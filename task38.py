# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
# Формат сдачи: pull-request.

phone_book = {}
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    for i, contact in enumerate(contacts, 1):
        phone_book[i] = contact.strip().split(';')
    
def save_file():
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)    
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def show_contacts(pb: dict):
    for i, contact in pb.items():
        print(f'{i:>3}.{contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')

def new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон: ')
    comment = input('введите комментарий: ')
    u_id = max(phone_book.keys()) + 1
    phone_book[u_id] = [name, phone, comment]
    return name

def find_contact():
    result = {}
    word = input('Введите ключевое слово для поиска: ').lower()
    for i, contact in phone_book.items():
        if word in ''.join(contact).lower():
            result[i] = contact
    return result

def edit_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input('Введите ID контакта для изменения: '))
    current_name, current_phone, current_comment = phone_book[u_id]
    name = input('Введите новое имя контакта: ')
    phone = input('Введите новый телефон: ')
    comment = input('Введите новый комментарий: ')
    phone_book[u_id] = [name if name else current_name, phone if phone else current_phone, comment if comment else current_comment]
    return name if name else current_name

def del_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input('Введите ID контакта для удаления: '))
    name = phone_book.pop(u_id)
    return name[0] 



menu = '''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''

while True:
    print(menu)
    choice = input("Выберите пункт меню: \n")
    if choice == '1':
        open_file()
        print('\nТелефонная книга успешно загружена.\n')
    elif choice == '2':
        save_file()
        print('\nТелефонная книга успешно сохранена.\n')
    elif choice == '3':
        show_contacts(phone_book)
    elif choice == '4':
        name = new_contact()
        print(f'\nКонтакт {name} удачно создан.\n')
    elif choice == '5':
        result = find_contact()
        show_contacts(result)
    elif choice == '6':
        name = edit_contact()
        print(f'\nКонтакт {name} успешно изменен!\n')
    elif choice == '7':
        name = del_contact()
        print('\nУдалено ')
    elif choice == '8':
        print('\nДо свидания!\n')
        break
    else:
        print('\nОшибка ввода')    

