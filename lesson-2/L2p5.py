my_list = [7, 5, 3, 3, 2]
m = 'y'
print("Текущий рейтинг:", my_list)
while m == 'y':
    i = int(input("Введите новый элемент рейтинга:"))
    n = 0
    for el in my_list:
        if i > el:
            my_list.insert(n, i)
            i = 0
        n = n + 1
    if i != 0:
        my_list.append(i)
    print("Текущий рейтинг:", my_list)
    m = input("Если хотите закончить введите 'n', если хотите продолжить введите 'y':")
