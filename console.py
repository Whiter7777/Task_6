from model import set_database, show_markets, find_item, find_zip, decorator
from check_params import check_yes_no, check_number

start = input("Здравствуйте! Хотите начать работу? (y/n): ")
begin = check_yes_no(start)

Flag = False
if begin == "y":
    set_database("Export.csv")
    Flag = True
elif begin == "n":
    print("Всего хорошего!")

if Flag == True:

    print("Меню вызовов: "
          "\nshow - просмотр всех рынков"
          "\nfind_city - поиск рынков по городу"
          "\nfind_state - поиск рынков по штату"
          "\nfind_zip - поиск рынков по индексу"
          "\nend - выход из программы")

    view = input("Введите команду: ")

    while view != "end":

        if view == 'show':
            lst = show_markets("Markets.json")
            for i in lst:
                print(*i)
            view = input("Введите команду: ")

        elif view == "find_city":
            my_city = input("Введите название города: ")
            result = find_item("Markets.json", "Cities.csv", my_city, 7)
            for i in result:
                print(i)
            view = input("Введите команду: ")

        elif view == "find_state":
            my_state = input("Введите название штата: ")
            result = find_item("Markets.json", "States.csv", my_state, 9)
            for i in result:
                print(i)
            view = input("Введите команду: ")

        elif view == "find_zip":
            my_zip = input("Введите индекс: ")
            print("Дальность, в зоне которой нужно показывать рынки")
            distance = check_number()
            new_decorator = decorator("Coords.json", distance)
            decorated_function = new_decorator(find_zip)
            result = decorated_function("Markets.json", "Zips.csv", my_zip, 10)
            view = input("Введите команду: ")
