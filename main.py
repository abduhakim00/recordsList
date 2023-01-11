import sys
from grocery import Grocery


def start(args=None):
    print(f'Welcome to Your Grocery list')

    if args is not None:
        Grocery.set_filename(args[1])
        if args[2] not in ['add', 'delete', 'update', 'sum']:
            print("Второй аргумент должен быть одним из следующих вариантов: ['add', 'delete', 'update', 'sum'] ")
            return
        setAction = args[2]
    else:
        print("выберите операцию из списка!")
        setAction = input('add, delete, update, sum: ')
        if setAction not in ['add', 'delete', 'update', 'sum']:
            print("Операция должна быть одна из следующих вариантов: ['add', 'delete', 'update', 'sum'] ")
            return

    # инициализация класса
    groceryList = Grocery()

    # выбор действия
    name = input("Пожалуйста введите наименование продукта для совершения операции: ")
    while not name:
        name = input("Пожалуйста введите наименование продукта для совершения операции: ")
    if setAction == 'add':
        print('Введите все данные')
        new_data = get_data()
        groceryList.add_record(new_data)
    elif setAction == 'sum':
        Grocery.find_total()
    elif setAction == 'delete':
        groceryList.delete_record(name)
    else:
        print('Введите новые данные')
        new_data = get_data()
        groceryList.edit_record(name, new_data)


def get_data():
    while True:
        name = input("Наименование Продукта: ")
        price = input("Цена продукта: ")
        if name and price:
            print(name+'-'+price)
            return name+'-'+price
        else:
            print("Пожалуйста ответьте на все требования!")


if __name__ == '__main__':
    if len(sys.argv) == 3 or len(sys.argv) == 1:
        start(sys.argv) if len(sys.argv) == 3 else start()
    else:
        print(f'Мы ожидали либо 2 аргумента, либо без аргументов, но получили {len(sys.argv) - 1} ')
