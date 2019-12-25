import math

a = 1001
b = ''
c = int(input("Введите ответ "))

while a <= 9999:
    a = str(a)
    b = a[::-1]
    print(b)
    if int(a) - int(b) == c:
        print("ДРУГ = " + str(a))
        break
    print(str(a))
    a = int(a)
    a += 1
else: print("Ответа нет!")