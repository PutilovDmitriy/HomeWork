import math

a = float(input("Введите начала отвезка [a,b] = "))
b = float(input("Введите конец отвезка [a,b] = "))
h = float(input("Введите шаг h = "))
f = 0
x = a
print("%-5s%7s" % ("f(x)", "x"))
while x <= b:
    if a > b:
        print("Укажите правильный интервал")
        break
    x = math.radians(x)
    f = math.cos(2*x)
    x = round(math.degrees(x), 4)
    print("%-5s%3s%7s" % (round(f, 4), ' | ', round(x, 4)))
    x += h