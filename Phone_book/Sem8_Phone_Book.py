def actions():
    select = menu()
    while select < '6':
        phone_book = open('Book.txt', 'r', encoding='utf-8')
        if select == '1':
            print(show_book(phone_book))
        elif select == '2':
            data = input('Введите данные абонента: ')
            print(find_contact(data))   
        elif select == '3':
            old_data = input()
            new_data = input()
            print(change_contact(old_data, new_data))
        elif select == '4':
            print("Введите данные: ") 
            print("Фамилия: ") 
            surname = input()
            print("Имя: ")
            name = input()
            print("Телефон: ")
            phone = input()
            print("Описание: ")
            description = input()
            print(add_contact(surname, name, phone, description))
        elif select == '5':
            print('Введите название файла, в который вы хотите скопировать данные: ')
            filename = input()
            print(copy_book(filename))    

 
        phone_book.close()  
        select = menu() 
    
              

def menu():
    print('Выберите желаемое действие:\n'
          '1. Показать справочник\n'
          '2. Найти абонента\n'
          '3. Изменить данные\n'
          '4. Добавить абонента в справочник\n'
          '5. Копировать данные из справочника в другой файл\n'
          '6. Завершить работу\n')
    select = input()
    return select


def show_book(phone_book):
    try:
        with open('Book.txt','r',encoding='utf-8') as phout:
            phone_book = phout.readlines()
            return phone_book
    except FileNotFoundError:
        return None

def find_contact(data):
    try:
        with open('Book.txt','r',encoding='utf-8') as phout:
            phone_book = phout.readlines()
            for i in phone_book:
                if data in i:
                    return i.strip()
            else:
                return 'Абонента с такой фамилией не найдено.'
    except FileNotFoundError:
        return 'Файл не найден'     
    


def change_contact(old_data, new_data):
    try:
        with open('Book.txt', 'r', encoding='utf-8') as phin:
            phone_book = phin.readlines()
            update = []
        with open('Book.txt', 'a', encoding='utf-8') as phout:
            for i in phone_book:
                if old_data in i:
                    i = i.replace(old_data, new_data)  
                update.append(i)
            with open('Book.txt', 'w', encoding='utf-8') as phout:
                phout.writelines(update)   
                return 'Данные успешно изменены.'
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    
def add_contact(surname, name, phone, description):
    try:
        with open('Book.txt', 'a', encoding='utf-8') as phout:
            phout.write(f'{surname} {name} {phone} {description}\n')
            return 'Абонент успешно добавлен.'
    except FileNotFoundError:
        return 'Файл не найден'

def copy_book(filename):
    try:
        if not filename.endswith('.txt'):
            filename += '.txt'
        with open('Book.txt', 'r', encoding='utf-8') as phin:
            phone_book = phin.readlines()
        with open(filename, 'w', encoding='utf-8') as phout:
            phout.writelines(phone_book)
            return 'Данные успешно скопированы в указанный файл.'
    except FileNotFoundError:
        return 'Файл не найден'          
               
          



actions()