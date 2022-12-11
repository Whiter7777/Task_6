from model import set_database
from check_params import check_yes_no

start = input("Здравствуйте! Хотите начать работу? (y/n): ")

begin = check_yes_no(start)

if start == "y":
    set_database("Export.csv")
elif start == "n":
    print("Всего хорошего!")