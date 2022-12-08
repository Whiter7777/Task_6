import re
pattern = r"\"[^\"]*\""

dct={}

"""Чтение файла"""
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


for val in dct.values():
    print(val[19], val[20])
