dct = {}
with open("Export.csv", "r") as inf:
    for line in inf:
        line = line.strip().split(",")
        dct[line[0]] = line[1:]

def make_set(dct_name, index):
    """создание справочной таблицы"""
    set_name = set()
    for val in dct_name.values():
        set_name.add(val[index])
    result = [[count, value] for count, value in enumerate(set_name, start=1)]
    return result

streets = make_set(dct, 6)
cities = make_set(dct, 7)
countys = make_set(dct, 8)
states = make_set(dct, 9)
zips = make_set(dct, 10)

coords_set = set()
for val in dct.values():
    coords_set.add((val[19], val[20]))

coords = {count:value for count, value in enumerate(coords_set, start=1)}

products = [[count, value] for count, value in enumerate(dct['FMID'][23:57], start=1)]
grades = [[1, "*"], [2, "**"], [3, "***"], [4, "****"], [5, "******"]]










