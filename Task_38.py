def write_name():
    name = input("Введите имя: ")
    return name

def write_surname():
    surname = input("Введите фамилию: ")
    return surname
    
def write_phone():
    phone = input("Введите номер вашего телефона: ")
    return phone

def write_adress():
    adress = input("Введите адрес: ")
    return adress

def save_data():
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open("Phone_book.txt", "a", encoding="utf-8") as data:
        data.write(f"{name} {surname}: {phone}\n{adress}\n\n")

def print_data():
    with open("Phone_book.txt", "r", encoding="utf-8") as data:
        data_first = data.readlines()
        print(data_first)
        for line in data_first:
            print(line, end="")

def search_line():
    search = input("Введите данные для поиска: ")
    with open("Phone_book.txt", "r", encoding="utf-8") as data:
        print(data)
        temp = data.readlines()
        print(temp)
        data_first = "".join(temp).split("\n\n")[:-1]
        print(data_first)
        for line in data_first:
            if search in line:
                print(line)
            # print(line, end="")

# print_data()
# search_line()


def modify_data():
    search = input("Введите имя или фамилию контакта, данные которого вы хотите изменить: ")
    with open("Phone_book.txt", "r+", encoding="utf-8") as data:
        lines = data.readlines()
        data.seek(0)
        for line in lines:
            if search in line:
                print(line)
                parts = line.split(":")
                field = input("Введите поле, которое вы хотите изменить (имя, фамилия, телефон, адрес): ")
                if field == "имя":
                    new_name = input("Введите новое имя: ")
                    line = f"{new_name} {parts[1]}"
                elif field == "фамилия":
                    new_surname = input("Введите новую фамилию: ")
                    line = f"{parts[0]}: {new_surname}"
                elif field == "телефон":
                    new_phone = input("Введите новый номер телефона: ")
                    line = f"{parts[0]}: {new_phone}"
                elif field == "адрес":
                    new_address = input("Введите новый адрес: ")
                    line = f"{parts[0]}: {parts[1]}\n{new_address}\n"
                data.write(line)
            else:
                data.write(line)
        data.truncate()
    print("Контакты успешно изменены.")

def delete_data():
    search = input("Введите имя или фамилию контакта, который вы хотите удалить: ")
    with open("Phone_book.txt", "r+", encoding="utf-8") as data:
        lines = data.readlines()
        data.seek(0)
        for line in lines:
            if search in line:
                print(line)
                confirm = input("Вы уверены что хотите удалить этот контакт? (да/нет): ")
                if confirm.lower() == "да":
                    for _ in range(3):
                        next(data)
                else:
                    data.write(line)
            else:
                data.write(line)
        data.truncate()
    print("Контакт успешно удален.")

modify_data()
delete_data()
