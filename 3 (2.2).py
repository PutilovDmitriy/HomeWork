import math

x = float(input("Введите X "))

if x <= -3:
    print("f(x) = 9")
else:
    f = 1 / (x**2 + 1)
    print("f(x) = " + str(f))
