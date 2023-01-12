import sys
from grocery import Grocery
FILENAME = 'groceriesList.txt'


def start(args=None):
    print(f'Welcome to Your Grocery list')
    while True:

        if args is not None:
            Grocery.set_filename(args[1])
            if args[2] not in ['add', 'delete', 'update', 'sum']:
                print("Второй аргумент должен быть одним из следующих вариантов: ['add', 'delete', 'update', 'sum'] ")
                return
            setAction = args[2]
            args = None
        else:
            print('~'*20)
            print("выберите операцию из списка!")
            print('Для выхода введите цифру 1!')
            print('~'*20)

            setAction = input('add, delete, update, sum: ')
            if setAction not in ['add', 'delete', 'update', 'sum', '1']:
                print("Операция должна быть одной из следующих вариантов: ['add', 'delete', 'update', 'sum'] ")
                return

        # инициализация класса
        groceryList = Grocery()

        # выбор действия
        if setAction == '1':
            break
        elif setAction == 'add':
            print('Введите все данные')
            new_data = get_data()
            groceryList.add_record(new_data)
        elif setAction == 'sum':
            Grocery.find_total()
        elif setAction == 'delete':
            name = input("Пожалуйста введите наименование продукта для совершения операции: ")
            while not name:
                name = input("Пожалуйста введите наименование продукта для совершения операции: ")
            groceryList.delete_record(name)
        else:
            name = input("Пожалуйста введите наименование продукта для совершения операции: ")
            while not name:
                name = input("Пожалуйста введите наименование продукта для совершения операции: ")
            print('Введите новые данные')
            new_data = get_data()
            groceryList.edit_record(name, new_data)


def get_data():
    while True:
        name = input("Наименование Продукта: ")
        price = input("Цена продукта: ")
        if len(name.split('-')) == 1 and price.isnumeric():
            print(name+'-'+price)
            return name+'-'+price
        else:
            print("Пожалуйста убедитесь что цена указана правильно и что в наименовании продукта нет дефизов!")


if __name__ == '__main__':
    if len(sys.argv) == 3 or len(sys.argv) == 1:
        start(sys.argv) if len(sys.argv) == 3 else start()
    else:
        print(f'Мы ожидали либо 2 аргумента, либо никаких аргументов, но получили {len(sys.argv) - 1} ')
