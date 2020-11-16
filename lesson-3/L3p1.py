def my_div(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print("Результат  = + бесконечность")
        return 0
    return a / b


res = my_div(float(input("Введите делимое: ")), float(input("Введите делитель: ")))
if res != 0:
    print("Равно = ", res)
    print("Округленно = ", round(res, 2))
