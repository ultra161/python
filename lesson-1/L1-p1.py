s1 = input("Введите строку 1: ")
s2 = input("Введите строку 2: ")
a1 = int(input("Введите целое число: "))
a2 = int(input("Введите целое отрицательное число: "))
a3 = float(input("Ведите число с плавающей точкой: "))
print("Вы ввели:")
print(s1)
print(s2)
if a1 >= 0:
    print(a1)
else:
    print("Вы ошиблись")
if a2 < 0:
    print(a2)
else:
    print("Вы ошиблись")
print(a3)
