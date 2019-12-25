import math

a = float(input("Введите угол a "))
b = float(input("Введите угол b "))

if (a + b) < 180:
   c = 180 - a - b
   if c == 90:
       print("Треугольник прямоугольный")
   else:
       print("Треугольник не прямоугольный")
else:
    print("Треугольник не возможен")