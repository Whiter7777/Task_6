def make_set(dct_name, index, column_name):
    """создание справочной таблицы"""
    set_name = set()
    for val in dct_name.values():
        if val[index] != column_name:
            set_name.add(val[index])
        result = [[count, value] for count, value in enumerate(set_name, start=1)]
    return result

def in_keys(dct_name, index, lst):
    """сопоставление ключей"""
    for val in dct_name.values():
        for i in lst:
            if val[index] == i[1]:
                val[index] = i[0]
    return dct_name

def set_mark_prod(lst, dct, index, number):
    """сопоставление market - product"""
    for key, val in dct.items():
        if val[index] == "Y":
            lst.append([key, products[number][0]])
    return lst