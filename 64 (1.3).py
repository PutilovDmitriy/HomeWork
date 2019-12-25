import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
s1 = a * b
s2 = a * c
s3 = b * c
m = [s1, s2, s3]

if m[0] == m[1]:
    reply = True
elif m[1] == m[2]:
    reply = True
elif m[0] == m[2]:
    reply = True
else:
    reply = False
print(reply)


