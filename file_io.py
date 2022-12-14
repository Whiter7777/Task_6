import re
import json
import pandas as pd

def read_main_file_csv(file_name: str):
    """Чтение из основного файла csv"""
    dct = {}
    pattern = r"\"[^\"]*\""
    with open(file_name, "r") as inf:
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
    return dct

def write_in_csv(file_name: str, lst: list):
    """Запись из списка в файл csv"""
    with open(file_name+".csv", "w") as inf:
        for i in lst:
            inf.write(str(i[0])+","+str(i[1])+"\n")

def read_file_csv(file_name: str):
    """чтение из файла csv в список"""
    lst = []
    with open(file_name, "r") as inf:
        for i in inf:
            line = i.strip().split(",")
            lst.append(line)
    return lst

def write_in_json(name: str, dct: dict):
    """Запись словаря в файл json"""
    with open(name, 'w') as outfile:
        json.dump(dct, outfile, ensure_ascii = False, indent=2)

def read_json(name: str):
    """Чтение словаря из файла json"""
    with open(name, "r") as file_in:
        inf = json.load(file_in)
        if len(inf) != 0:
            dct = inf
        else:
            dct = {}
    return dct

def write_grade(market_name, grade, file_name = "Markets.json", grade_file_name = "Grades.csv"):
    flag = False
    with open(file_name, "r") as file_in:
        inf = json.load(file_in)
        grade_lst = read_file_csv(grade_file_name)
        for key, val in inf.items():
            if market_name == val[0]:
                for i in grade_lst:
                    if i[1] == grade:
                        val[12] = int(i[0])
                        flag = True
    if flag == True:
        with open(file_name, 'w') as outfile:
            json.dump(inf, outfile, ensure_ascii=False, indent=2)
        return "Оценка добавлена"
    else:
        return "Введено неверное значение, оценка не добавлена"


def write_notice(market_name, notice, file_name = "Markets.json"):
    flag = False
    with open(file_name, "r") as file_in:
        inf = json.load(file_in)
        for key, val in inf.items():
            if market_name == val[0]:
                val[13] = notice
                flag = True
    if flag == True:
        with open(file_name, 'w') as outfile:
            json.dump(inf, outfile, ensure_ascii=False, indent=2)
        return "Рецензия добавлена"
    else:
        return "Введено неверное название рынка, оценка не добавлена"



