a = float(input("Ведите растояние за первый день:"))
b = float(input("Ведите растояние которое необходимо достичь:"))
n = 1
while True:
    if a > b: break
    a = a + a / 10
    n = n + 1
    continue
print("Спортсмену понадобится", n, "дней")
