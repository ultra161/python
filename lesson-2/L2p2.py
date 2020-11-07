s = input("Введите значеня через запятую:")
my_list = s.split(',')
new_list = []
n = 0
for el in my_list:
    if n % 2 == 0:
        n = n + 1
    else:
        new_list.insert(n - 1, my_list[n])
        new_list.insert(n, my_list[n - 1])
        n = n + 1
if n % 2 != 0:
    new_list.append(my_list[n - 1])
print("My_list: ", my_list)
print("")
print("New_list:", new_list)