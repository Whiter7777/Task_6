from file_io import read_file_csv, read_json
from model import relations


def view_info(name):
    view_lst = []
    markets = read_json("Markets.json")
    coords = read_json("Coords.json")
    streets = read_file_csv("Streets.csv")
    cities = read_file_csv("Cities.csv")
    countys = read_file_csv("Countys.csv")
    states = read_file_csv("States.csv")
    zips = read_file_csv("Zips.csv")
    products = read_file_csv("Products.csv")
    for key, val in markets.items():
        if val[0] == name:
            view_lst.extend([key, val[0], val[1], val[2], val[3], val[4], val[5]])
            view_lst.append(*relations("Markets.json", streets, 7, name))
    return view_lst


print(*view_info("Ames Main Street Farmers' Market"))