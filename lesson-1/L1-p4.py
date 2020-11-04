a = int(input("Введите целое положительное число:"))
b = 0
x = 0
while True:
    if a < 10: break
    b = a % 10
    if b > x: x = b
    a = a // 10
    continue
if a > x: x = a
print(x)
