import math

a = float(input("Участник 1 = "))
b = float(input("Участник 2 = "))
c = float(input("Участник 3 = "))

mas = [a, b , c]
mas = sorted(mas)

print("Результат победителя = " + str(mas[0]))
