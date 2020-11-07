in_sec = int(input("Введите количество секунд:"))
out_sec = in_sec % 60
out_min = (in_sec // 60) % 60
out_h = (in_sec // 60) // 60
print('Результат равен=', out_h, 'часов:', out_min, 'минут:', out_sec, 'секунд:')
