import math

print("Введите высоту и радиус")
h = float(input("h = "))
r = float(input("r = "))

if h <= 0 or r <= 0:
    print("Решений не существует")
else:
    V1 = math.pi * math.pow(r , 2) * h
    V2 = V1 / 3
    print("Объем цилиндра = " + str(V1) + "Объем пирамиды = " + str(V2))
