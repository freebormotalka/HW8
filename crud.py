import csv
import os.path


db_file_name = ''
db = []
global_id = 0  # id для добавления пользователей


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("ALARM NO NAME SPECIFIED")
        return
    if(surname == ''):
        print("ALARM NO SURNAME SPECIFIED")
        return
    if(number == ''):
        print("ALARM NO TELEPHONE NUMBER SPECIFIED!")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number):
            print("already exist")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
                surname.title(), number]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


# поиск (если нужно выгрузить все: result = retrive())
def retrive(id='', name='', surname='', number=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        # выход список списков
        return result


def update(id='', new_name='', new_surname='', new_number=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_surname != ''):
                    row[2] = new_surname.title()

                if(new_number != ''):
                    row[3] = new_number
            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def get_token():
    file = open('token.csv', 'r', encoding='utf-8')
    for i in file:
        token = i
    file.close()
    return token

def copy_line(source_file, target_file, row):
    with open(source_file, 'r') as file:
        lines = file.readlines()
# Проверка корректности номера строки
    if row < 2 or row > len(lines):
        print ('Некорректный номер строки')
        return
# Открытие целевого файла для записи
    with open(target_file, 'w') as file:
        # Копирование выбранной строки в целевой файл
        file.write(lines[row -1])
        # Запись оставшихся строк
        # for i in range(len(lines)):
        #     if i != row - 1:
        #         file.write(lines[i])
    print('Копирование строки успешно выполнено')



    # ====================ПРИМЕР ИСПОЛЬЗОВАНИЯ НИЖЕ=======================
    # init_data_base("test.csv") # инициализация базы

    # =================Примеры создания записей=================
    # create('vasya','pupkin','123')
    # create('vasya','pupkin','1232432')
    # create('vasya','pupkin','1')
    # create('vasya','pup','123')
    # create('vas1','123')

    # ==================Примеры поиска записей===============
    # print(retrive()) # Выбор всего что есть
    # print(retrive(number='123'))
    # print(retrive(id='123'))
    # print(retrive(id='1', number='123'))

    # ==================Обновление записи==================
    # update(id='2', new_number='09876544', new_name='petya')

    # ===================Удаление записи=======================
    # delete('1')
    # ===================Замена строк в файле==================
    # source_file = 'source.txt'
    # target_file = 'target.txt'
    # line_number = int(input('Введите номер строки: '))
    # copy_line(source_file, target_file, line_number)