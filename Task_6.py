import csv

dct = {}

# with open("Export.csv", "r") as inf:
#     for i in inf:
#         line = i.strip().split(",")
#         dct[line[0]] = line[1:]

with open("Export.csv", "r") as a:
    reader = csv.reader(a)
    for row in reader:
        dct[row[0]] = row[1:]

asd = csv.reader("")

def make_set(dct_name, index, column_name):
    """создание справочной таблицы"""
    set_name = set()
    for val in dct_name.values():
        if val[index] != column_name:
            set_name.add(val[index])
        result = [[count, value] for count, value in enumerate(set_name, start=1)]
    return result

streets = make_set(dct, 6, 'street')
cities = make_set(dct, 7, 'city')
countys = make_set(dct, 8, 'County')
states = make_set(dct, 9, 'State')
zips = make_set(dct, 10, 'zip')

{coords_set = set()
for val in dct.values():
    coords_set.add((val[19], val[20]))

coords = {count:value for count, value in enumerate(coords_set, start=1)}

products = [[count, value] for count, value in enumerate(dct['FMID'][23:57], start=1)]
grades = [[1, "*"], [2, "**"], [3, "***"], [4, "****"], [5, "******"]]

"""Таблица markets"""
markets = {}
for key, val in dct.items():
    markets[key] = (val[0:11])

"""Заполняем таблицу ключами из сводных таблиц"""

def in_keys(dct_name, index, lst):
    for val in dct_name.values():
        for i in lst:
            if val[index] == i[1]:
                val[index] = i[0]
    return dct_name

in_keys(markets, 6, streets)
in_keys(markets, 7, cities)
in_keys(markets, 8, countys)
in_keys(markets, 9, states)
in_keys(markets, 10, zips)

for key, val in markets.items():
    val.append("")
    val.append("")
    val.append("")

markets['FMID'] = ['MarketName', 'Website', 'Facebook', 'Twitter', 'Youtube', 'OtherMedia', 'street', 'city', 'County', 'State', 'zip', 'coоrds', 'grade', 'comment']

