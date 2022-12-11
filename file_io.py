import re
import json

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
            dict = inf
        else:
            dict = {}
    return dict


