import random
import math

n = int(input("Введите размер массива n = "))
k = int(input("Введите верхний предел чисел масива = "))
list = []
i = 0
while i < n:
    x = random.randint(1, k)
    list.append(x)
    i += 1

list = sorted(list)
j = 0
s = 0
while j < n:
    if list[0] == list[j]:
        s += 1
    j += 1
print(str(s) + " раз встречается минимальный элемент в последовательности")