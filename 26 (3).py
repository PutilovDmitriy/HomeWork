import math
print("Введите дату")
d = int(input())
print("Введите месяц")
m = int(input())

mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

i = 0
while i < m - 1:
    day += mon[i]
    i += 1
else:
    day += d

print("В " + str(d) + " день " + str(m) + " месяца, будет " + str(day) + " день года.")