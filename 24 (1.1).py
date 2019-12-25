import math

x = float(input("X = "))

a = (x - 10 * math.sin(math.radians(x)) + math.fabs(x**4 - x**5))
print(a)