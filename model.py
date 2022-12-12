from file_io import read_main_file_csv, read_file_csv, read_json, write_in_csv, write_in_json
from func_for import make_set, set_mark_prod, in_keys

def set_database(mail_file_name: str):
    dct = read_main_file_csv(mail_file_name) #Читаем основную таблицу

    streets = make_set(dct, 6, 'street') #Справочная таблица улиц
    write_in_csv("Streets", streets) #Импорт справочной таблицы в csv

    cities = make_set(dct, 7, 'city') #Справочная таблица городов
    write_in_csv("Cities", cities) #Импорт справочной таблицы в csv

    countys = make_set(dct, 8, 'County') #Справочная талица округов
    write_in_csv("Countys", countys) #Импорт справочной таблицы в csv

    states = make_set(dct, 9, 'State') #Справочная талица штатов
    write_in_csv("States", states) #Импорт справочной таблицы в csv

    zips = make_set(dct, 10, 'zip') #Справочная талица индексов
    write_in_csv("Zips", zips) #Импорт справочной таблицы в csv

    coords_set = set()
    for val in dct.values():
        coords_set.add((val[19], val[20]))
    coords = {count: value for count, value in enumerate(coords_set, start=1)} #Справочная словарь с координатами
    write_in_json("Coords", coords) #Импорт справочного словаря в json

    products = [[count, value] for count, value in enumerate(dct['FMID'][23:57], start=1)] #Справочная таблица с продуктами
    write_in_csv("Products", products)

    grades = [[1, "*"], [2, "**"], [3, "***"], [4, "****"], [5, "******"]] #Справочная таблица оценок
    write_in_csv("Grades", grades) #Импорт справочной таблицы в csv

    """Таблица markets"""
    markets = {}
    for key, val in dct.items():
        markets[key] = (val[0:11])

    """Заполняем таблицу ключами из сводных таблиц"""

    in_keys(markets, 6, streets)
    in_keys(markets, 7, cities)
    in_keys(markets, 8, countys)
    in_keys(markets, 9, states)
    in_keys(markets, 10, zips)

    for key, val in markets.items():
        val.append("")
        val.append("")
        val.append("")

    """Добавляем ключи координат"""
    for val in dct.values():
        for k, v in coords.items():
            if val[19] == v[0] and val[20] == v[1]:
                val.append(k)

    for key, val in dct.items():
        for k, v in markets.items():
            if key == k:
                v[11] = val[-1]

    markets['FMID'] = ['MarketName', 'Website', 'Facebook', 'Twitter', 'Youtube', 'OtherMedia', 'street', 'city',
                       'County', 'State', 'zip', 'coоrds', 'grade', 'comment']

    write_in_json("Markets.json",  markets)  # Импорт справочного словаря в json

    """Таблица markets - products (многие ко многим)"""
    mark_prod = []
    index = 23
    number = 0
    for i in range(len(products)):
        set_mark_prod(mark_prod, dct, index, number, products)
        index += 1
        number += 1

    write_in_csv("Mark_prod", mark_prod) #Импорт справочной таблицы в csv

def show_markets(file_name):
    """Просмотр рынков"""
    lst = []
    dct = read_json(file_name)
    for val in dct.values():
        lst.append([val[0], val[12], val[13]])
    return lst

def find_item(file_name, table_name, my_var, index):
    markets = read_json(file_name)
    params = read_file_csv(table_name)
    lst = []
    for i in params:
        if my_var == i[1]:
            my_var_index = int(i[0])
    for val in markets.values():
        try:
            if my_var_index == val[index]:
                lst.append(val[0])
        except UnboundLocalError:
            lst.append("Неверно введено значение, повторите вызов команды")
            break
    return lst






