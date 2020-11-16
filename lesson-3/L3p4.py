def my_func(x, y):
    z = 1
    while y != 0:
        z = z * x
        y += 1
    return 1 / z


print(my_func(float(input("Введите действительное положительное число:= ")),
              int(input("Введите целое орицательное число:= "))))
