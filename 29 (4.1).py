import math

a = 1001
b = ''
uniq = False
while a <= 9999:
    a = str(a)
    b = a[::-1]
    if int(a) - int(b) == 2727:
        a = str(a)
        if int(a[3]) != 0 and a[0] != a[1] and a[0] != a[2] and a[0] != a[3] and a[1] != a[2] and a[1] != a[3] and a[2] != a[3]:
            print("ДРУГ = " + str(a))

    a = int(a)
    a += 1