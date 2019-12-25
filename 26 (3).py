import math

d = int(input("Введите месяц "))
m = int(input("Введите месяц "))

mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

i = 0
while i < m - 1:
    day += mon[i]
    i += 1
else:
    day += d

print("В " + str(d) + " день " + str(m) + " месяца, будет " + str(day) + " день года.")