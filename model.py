from file_io import read_main_file_csv, read_file_csv, read_json, write_in_csv, write_in_json
from func_for import make_set, set_mark_prod, in_keys
from haversine import haversine, Unit

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
    write_in_json("Coords.json", coords) #Импорт справочного словаря в json

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
    """Поиск по списку из файла"""
    markets = read_json(file_name)
    params = read_file_csv(table_name)
    lst = []
    for i in params:
        if my_var.split(",") == i[1:]:
            my_var_index = int(i[0])
    for val in markets.values():
        try:
            if my_var_index == val[index]:
                lst.append(val[0])
        except UnboundLocalError:
            lst.append("Неверно введено значение, повторите вызов команды")
            break
    return lst

def decorator(file_coords, distance = 30):
    """Поиск с учетом дистанции"""
    def decorator_index(func):
        def wrapper(file_name, table_name, my_var, index):
            markets = read_json(file_name)
            coords = read_json(file_coords)
            lst_coords = []
            lst_markets = []
            lst = func(file_name, table_name, my_var, index)
            for i in range(len(lst)):
                if lst[0] == "Неверно введено значение, повторите вызов команды":
                    return lst
                else:
                    for key, val in coords.items():
                        if int(key) == lst[0][1]:
                            start_coords = val
                            a = (float(start_coords[1]), float(start_coords[0]))
                    for key, val in coords.items():
                        if val[1] != "y"and val[1] != "":
                            b = (float(val[1]), float(val[0]))
                            if haversine(a, b, unit=Unit.MILES) <= distance:
                                lst_coords.append(key)
                    for val in markets.values():
                        for i in lst_coords:
                            if val[11] == int(i):
                                lst_markets.append(val[0])
            return lst_markets
        return wrapper
    return decorator_index

# @decorator("Coords.json")
def find_zip(file_name, table_name, my_var, index):
    """Поиск по индексу"""
    markets = read_json(file_name)
    params = read_file_csv(table_name)
    lst = []
    for i in params:
        if my_var == i[1]:
            my_var_index = int(i[0])
    for val in markets.values():
        try:
            if my_var_index == val[index]:
                lst.append([val[0], val[11]])
        except UnboundLocalError:
            lst.append("Неверно введено значение, повторите вызов команды")
            break
    return lst

def relations(file_name, table_name, index, name):
    """Возвращение значения по ключу для списков"""
    markets = read_json(file_name)
    for val in markets.values():
        if val[0] == name:
            for i in table_name:
                if val[index] == int(i[0]):
                    return ",".join(i[1:])

def set_mark_prod_dct(mark_prod, products):
    """Возвращение значения по ключу для словаря из общей таблицы рынок-продукты"""
    dct_mark_prod = {}
    for i in mark_prod:
        dct_mark_prod.setdefault(i[0], []).append(i[1])
    for val in dct_mark_prod.values():
        for i in range(len(val)):
            for j in products:
                if val[i] == j[0]:
                    val[i]= j[1]
    return dct_mark_prod

def view_info(name):
    """Сбор информации о рынке"""
    view_lst = []
    markets = read_json("Markets.json")
    coords = read_json("Coords.json")
    streets = read_file_csv("Streets.csv")
    cities = read_file_csv("Cities.csv")
    countys = read_file_csv("Countys.csv")
    states = read_file_csv("States.csv")
    zips = read_file_csv("Zips.csv")
    grades = read_file_csv("Grades.csv")
    products = read_file_csv("Products.csv")
    mark_prod = read_file_csv("Mark_prod.csv")
    dct_mark_prod = set_mark_prod_dct(mark_prod, products)
    for key, val in markets.items():
        if val[0] == name:
            view_lst.extend([key, val[0], val[1], val[2], val[3], val[4], val[5]])
            view_lst.append(relations("Markets.json", streets, 6, name))
            view_lst.append(relations("Markets.json", cities, 7, name))
            view_lst.append(relations("Markets.json", countys, 8, name))
            view_lst.append(relations("Markets.json", states, 9, name))
            view_lst.append(relations("Markets.json", zips, 10, name))
    for key, val in markets.items():
        if val[0] == name:
            for k, v in coords.items():
                if val[11] == int(k):
                    view_lst.append(v[0])
                    view_lst.append(v[1])
    for key, val in markets.items():
        if val[0] == name:
            for k, v in dct_mark_prod.items():
                if key == k:
                    view_lst.extend(v)
    for key, val in markets.items():
        if val[0] == name:
            view_lst.append(relations("Markets.json", grades, 12, name))
            view_lst.append(val[13])
    if len(view_lst) == 0:
        return ["По данному рынку нет информации"]
    else:
        return view_lst



