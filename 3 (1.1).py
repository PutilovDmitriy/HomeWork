import math
print("X = ")
x = math.radians(float(input()))
print("Y = ")
y = math.radians(float(input()))
print(math.cos(x))
print(math.sin(y))
if (math.cos(x) - math.sin(y)) == 0:
    print("Решений не существует")
elif x*y % math.radians(180) == math.radians(90):
    print("Решений не существует")
else:
    a = ((math.sin(x) - math.cos(y)) / (math.cos(x) - math.sin(y) )) * math.tan(x*y)
    print(a)