import math
print("Участник 1 = ")
a = float(input())
print("Участник 2 = ")
b = float(input())
print("Участник 3 = ")
c = float(input())

mas = [a, b , c]
mas = sorted(mas)

print("Результат победителя = " + str(mas[0]))
