def my_func():
    f = True
    my_sum = 0
    while f:
        s = input("Введите значеня через пробел, для выхода введите q:")
        my_list = s.split()
        for el in my_list:
            if el == "q":
                f = False
            else:
                a = int(el)
                my_sum = my_sum + a
    print(my_sum)
    return my_sum


my_func()
