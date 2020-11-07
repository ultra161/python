s = input("Введите строку из нескольких слов, разделённых пробелами:")
my_list = s.split(' ')
# print(my_list)
n = 1
for el in my_list:
    print(n, el[0:10])
    n = n + 1
