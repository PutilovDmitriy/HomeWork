import math
print("Введите высоты")
print("a")
a = float(input())
print("b")
b = float(input())
print("c")
c = float(input())

if a <= 0 or b <= 0 or c <= 0:
    print("Решений не сушествует")
else:
    p = (a+b+c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    h1 = 2*s / a
    h2 = 2*s / b
    h3 = 2*s / c
    print("h1 = " + str(h1) + "h2 = " + str(h2) + "h3 = " + str(h3))
