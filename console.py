from model import set_database, show_markets, find_item, find_zip, decorator, view_info
from check_params import check_yes_no, check_number
from  file_io import write_grade, write_notice

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
          "\ninfo - вывод полной информации о рынках по предыдущему запросу"
          "\nmarket - просмотр полной информации о конкретном рынке"
          "\ngrade - оценить рынок"
          "\nnotice - написать рецензию"
          # "\ndel - удалить запись"
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
            lst = result
            for i in result:
                print(i)
            view = input("Введите команду: ")

        elif view == "find_state":
            my_state = input("Введите название штата: ")
            result = find_item("Markets.json", "States.csv", my_state, 9)
            lst = result
            for i in result:
                print(i)
            view = input("Введите команду: ")

        elif view == "find_zip":
            my_zip = input("Введите индекс: ")
            print("Дальность (миль), в зоне которой нужно показывать рынки")
            distance = check_number()
            new_decorator = decorator("Coords.json", distance)
            decorated_function = new_decorator(find_zip)
            result = decorated_function("Markets.json", "Zips.csv", my_zip, 10)
            lst = result
            for i in result:
                print(i)
            view = input("Введите команду: ")

        elif view == "market":
            name = input("Введите название рынка: ")
            result = view_info(name)
            print(*result)
            view = input("Введите команду: ")

        elif view == "info":
            for i in lst:
                result = view_info(i)
                print(*result)
            view = input("Введите команду: ")

        elif view == "grade":
            market_name = input("Введите название рынка: ")
            grade = input("Введите оценку: ")
            result = write_grade(market_name, grade)
            print(result)
            view = input("Введите команду: ")

        elif view == "notice":
            market_name = input("Введите название рынка: ")
            notice = input("Напишите рецензию: ")
            result = write_notice(market_name, notice)
            print(result)
            view = input("Введите команду: ")




