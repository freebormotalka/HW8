import random
import csv


file = open('base_phone.csv', 'w', encoding='utf-8')
newrecord = "ID,Name,Surname,PhoneNumber\n"
file.writelines(newrecord)

ls_name = ['Ivan', 'Fedor', 'Mihail', 'Lev', 'Alexandr',
            'Anton', 'Nikolay', 'Miron']
ls_surname = ['Bunin', 'Dostoevskiy', 'Bulgakov',
                'Tolstoy', 'Pushkin', 'Chehov', 'Duma', 'Gogol', 'Kuprin']


def list_of_numbers():
    # s = '+'
    randomListPhone = random.randint(79000000000, 80000000000)
    # s = s + str(randomListPhone)
    return str(randomListPhone)
# рандомно соеденить имена фамилии и номера телефонов (отдельный метод) def + присвоение id


def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + \
        list_of_numbers()
    return s


def start():
    for i in range(20):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


start()