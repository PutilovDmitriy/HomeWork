import math
print("Введите X")
x = float(input())

if x <= -3:
    print("f(x) = 9")
else:
    f = 1 / (x**2 + 1)
    print("f(x) = " + str(f))
