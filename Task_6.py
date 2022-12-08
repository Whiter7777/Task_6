import csv
import re
from func_for import make_set
from func_for import in_keys

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

# with open("Export.csv", "r") as inf:
#     for i in inf:
#         line = i.strip().split(",")
#         dct[line[0]] = line[1:]

# with open("Export.csv", "r") as a:
#     reader = csv.reader(a)
#     for row in reader:
#         dct[row[0]] = row[1:]

"""создание справочной таблицы"""
streets = make_set(dct, 6, 'street')
cities = make_set(dct, 7, 'city')
countys = make_set(dct, 8, 'County')
states = make_set(dct, 9, 'State')
zips = make_set(dct, 10, 'zip')

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

# for key, val in markets.items():
#     val.append("")
#     val.append("")
#     val.append("")
#
# markets['FMID'] = ['MarketName', 'Website', 'Facebook', 'Twitter', 'Youtube', 'OtherMedia', 'street', 'city', 'County', 'State', 'zip', 'coоrds', 'grade', 'comment']

