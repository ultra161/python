def my_func(a, b, c):
    return a + b + c - min(a, b, c)


print("Сумма двух больших чисел = ",
      my_func(int(input("Введите целое число: ")), int(input("Введите второе целое число: ")),
              int(input("Введите третье целое число: "))))
