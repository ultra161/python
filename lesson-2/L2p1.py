
my_list = [1, 2.3, "text", True, [True, False], 1 + 2j, ('dec', 'jan', 'feb'), {'а', 'б', 'в'}, None,
           {"z": 1, "x": 2, "c": 3}]
for n in my_list:
    print("Для значения:", n)
    print("Установлен тип данных", type(n))
    print("")
