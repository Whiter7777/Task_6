def check_yes_no(s: str):
    if s == "y":
        return s
    elif s == "n":
        return s
    else:
        s = input("Попробуйте еще раз. Хотите начать работу? (y/n): ")
        return check_yes_no(s)

def check_number():
    """Проверка вводимого числа"""
    while True:
        try:
            n = int(input("Введите целое число: "))
            break
        except ValueError:
            print("Это не целое число, попробуйте еще раз")
    return n


