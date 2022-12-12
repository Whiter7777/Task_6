import math as m
from haversine import haversine, Unit

a = (-77.189254, 40.201689)
b = (-84.376724, 33.725504)

print(haversine(a, b, unit=Unit.MILES))

from model import set_database, show_markets, find_item, decorator, find_zip
from check_params import check_yes_no


my_zip = input("Введите индекс: ")
new_decorator = decorator("Coords.json", 100)
decorated_function = new_decorator(find_zip)
result = decorated_function("Markets.json", "Zips.csv", my_zip, 10)

print(result)

