def my_func(s):
    s = s.capitalize()
    # print(s)
    return s


new_list = ''
my_list = input("Введите строку").split()
for el in my_list:
    new_list = new_list + my_func(el) + ' '
print(new_list)
