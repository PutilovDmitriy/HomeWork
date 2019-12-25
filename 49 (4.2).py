import math

a = float(input("Введите действительное число a "))
n = int(input("Введите натуральное число n "))
s = 0
i = 1
while i <= n:
    if n == 1:
        s = 1
        print("S = " + str(s))
        break
    if i == 1:
        s = 1/a
        i += 1
        continue
    s = s + 1/a**(2*i-2)
    i += 1
print("S = " + str(s))