import pandas as pd
import csv
import re


from func_for import make_set
from func_for import in_keys
from func_for import set_mark_prod
from file_io import write_in_csv, read_file_csv

# df = pd.read_csv("Export.csv")
#
# with open("Export.csv", "r") as a:
#     reader = csv.reader(a)
#     for row in reader:
#         dct[row[0]] = row[1:]

dct = {}
pattern = r"\"[^\"]*\""

with open("Export.csv", "r") as inf:
    for i in inf:
        line = i.strip()
        match = re.findall(pattern, line)
        my_match = []
        for i in match:
            if "," in i:
                j = i.replace(",", "$")
                my_match.append(j)
            else:
                my_match.append(i)
        for i in range(len(match)):
            if match[i] in line:
                line = line.replace(match[i], my_match[i])
        line = line.split(",")
        for i in range(len(line)):
            if "$" in line[i]:
                line[i] = line[i].replace("$", ",")
        dct[line[0]] = line[1:]

"""создание справочной таблицы"""
streets = make_set(dct, 6, 'street')
cities = make_set(dct, 7, 'city')
countys = make_set(dct, 8, 'County')
states = make_set(dct, 9, 'State')
zips = make_set(dct, 10, 'zip')

write_in_csv("streets", streets)
lst = read_file_csv("streets.csv")

for i in range(len(streets)):
    print(streets[i] == lst[i])

coords_set = set()
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

markets['FMID'] = ['MarketName', 'Website', 'Facebook', 'Twitter', 'Youtube', 'OtherMedia', 'street', 'city', 'County', 'State', 'zip', 'coоrds', 'grade', 'comment']

"""Таблица markets - products (многие ко многим)"""
mark_prod = []
index = 23
number = 0
for i in range(len(products)):
    set_mark_prod(mark_prod, dct, index, number, products)
    index += 1
    number += 1

# my_city = input("Введите название города: ")
# my_state = input("Введите название штата: ")
# my_zip = input("Введите индекс: ")
# my_round = input("Введите ограничение по удаленности: ")

# for i in cities:
#     if my_city == i[1]:
#         my_city_index = i[0]
#
# for i in states:
#     if my_state == i[1]:
#         my_state_index = i[0]
#
# for i in zips:
#     if my_zip == i[1]:
#         my_zip_index = i[0]
#
# """Поиск по 3-м параметрам"""
# for val in markets.values():
#     if my_city_index == val[7] and my_state_index == val[9] and my_zip_index == val[10]:
#         print(val[0])