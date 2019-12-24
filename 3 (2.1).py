import math
print("Введите угол a")
a = float(input())
print("Введите угол b")
b = float(input())

if (a + b) < 180:
   c = 180 - a - b
   if c == 90:
       print("Треугольник прямоугольный")
   else:
       print("Треугольник не прямоугольный")
else:
    print("Треугольник не возможен")